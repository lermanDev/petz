import django_filters
from django.db.models import Q
from .models import BlogPost
from django.forms.widgets import TextInput

class BlogFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='search_filter', 
        widget=TextInput(attrs={'placeholder': 'Search on blog...'}),
        required=True
    )

    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'category', 'tags']

    def search_filter(self, queryset, name, value):
        """
        Permite realizar una búsqueda difusa en los campos 'title' y 'author'.
        """
        return queryset.filter(Q(title__icontains=value))
