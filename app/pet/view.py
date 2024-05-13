from .filters import PetFilter
from .models import Pet, Specie
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
        pets_number = request.GET.get("pets_number", 2)
        filter = PetFilter(request.GET, queryset=Pet.objects.all())
        
        specie_filter = request.GET.get('specie')
        specie_filtered = None
        if specie_filter:
            specie_instance = Specie.objects.filter(id=specie_filter).first()
            if specie_instance:
                specie_filtered = specie_instance

        paginator = Paginator(filter.qs, pets_number)
        page = request.GET.get("page")
        try:
            pets_paginated = paginator.page(page)
        except PageNotAnInteger:
            pets_paginated = paginator.page(1)
        except EmptyPage:
            pets_paginated = paginator.page(paginator.num_pages)

        context = {"pet_list": pets_paginated, "filter": filter, "specie_filtered": specie_filtered}

        if request.htmx:
            return render(
                request,
                "pet/partials/list.html",
                context,
            )

        return render(
            request,
            "pet/pets.html",
            context,
        )


class PetView(DetailView):
    model = Pet
    context_object_name = "pet"
    template_name = "pet/pet_info.html"

    def get(self, request, *args, **kwargs):
        filter = PetFilter(request.GET, queryset=Pet.objects.all())
        pet = Pet.objects.get(id=kwargs["id"])

        if request.htmx:
            return render(
                request,
                "pet/partials/detail.html",
                {"pet": pet, "filter": filter},
            )

        return render(
            request,
            "pet/pet_info.html",
            {"pet": pet, "filter": filter},
        )
