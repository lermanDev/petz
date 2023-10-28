from .filters import PetFilter
from .models import Pet
from django_filters.views import FilterView


class PetListView(FilterView):
    model = Pet
    context_object_name = "pet_list"
    template_name = "pet/pet_list.html"
    filterset_class = PetFilter
