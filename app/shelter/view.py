from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Shelter
from .filters import ShelterFilter
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ShelterListView(FilterView, ListView):
    model = Shelter
    context_object_name = 'shelters'
    template_name = 'shelter/shelter.html'
    filterset_class = ShelterFilter

    def get(self, request):
        filter = ShelterFilter(request.GET, queryset=Shelter.objects.all())
        paginator = Paginator(filter.qs, 3)
        page = request.GET.get("page")
        try:
            shelter_paginated = paginator.page(page)
        except PageNotAnInteger:
            shelter_paginated = paginator.page(1)
        except EmptyPage:
            shelter_paginated = paginator.page(paginator.num_pages)

        # Determining if filtering is applied
        is_filtering = any(1 for key, value in request.GET.items() if key != 'page' and (value or value==''))

        # Determining if pagination is applied
        is_paginating = page is not None

        context = {"shelter_list": shelter_paginated, "filter": filter, "extends_base": "base.html"}

        if request.htmx:
            context["extends_base"] = "partials/empty_base.html"

        if (is_filtering or is_paginating) and request.htmx:
            return render(
                request,
                "shelter/partials/list.html",
                context,
            )
        
        return render(
            request,
            "shelter/shelter.html",
            context,
        )