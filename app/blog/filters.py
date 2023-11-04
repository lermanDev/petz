import django_filters
from .models import BlogPost


class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = BlogPost
        fields = ["author", "title", "category", "tags"]
