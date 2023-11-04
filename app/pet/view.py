from .filters import PetFilter
from .models import Pet
from django_filters.views import FilterView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView


class PetListView(FilterView):
    model = Pet
    context_object_name = "pets"
    template_name = "pet/pets.html"
    filterset_class = PetFilter

    def get(self, request):
        pets_number = request.GET.get("pets_number", 6)
        filter = PetFilter(request.GET, queryset=Pet.objects.all())
        paginator = Paginator(filter.qs, pets_number)
        page = request.GET.get("page")
        try:
            pets_paginated = paginator.page(page)
        except PageNotAnInteger:
            pets_paginated = paginator.page(1)
        except EmptyPage:
            pets_paginated = paginator.page(paginator.num_pages)

        if request.htmx:
            return render(
                request,
                "pet/partials/list.html",
                {"pet_list": pets_paginated},
            )

        return render(
            request,
            "pet/pets.html",
            {"pet_list": pets_paginated, "filter": filter},
        )


class PetView(DetailView):
    model = Pet
    context_object_name = "pet"
    template_name = "pet/pet_info.html"

    def get(self, request, *args, **kwargs):
        pet = Pet.objects.get(id=kwargs["id"])
        if request.htmx:
            return render(
                request,
                "pet/partials/detail.html",
                {"pet": pet},
            )

        return render(
            request,
            "pet/pet_info.html",
            {"pet": pet},
        )
