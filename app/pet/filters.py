import django_filters
from .models import Pet, Specie


class PetFilter(django_filters.FilterSet):
    class Meta:
        model = Pet
        fields = ["specie", "gender", "size", "shelter", "shelter__city"]