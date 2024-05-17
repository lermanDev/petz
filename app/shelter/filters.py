import django_filters
from .models import Shelter, State

class ShelterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Shelter Name")
    city = django_filters.CharFilter(lookup_expr='icontains', label="City")

    class Meta:
        model = Shelter
        fields = [
            'name',
            'city',
            'state'
        ]