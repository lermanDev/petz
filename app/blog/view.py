from .filters import BlogFilter
from .models import BlogPost
from django_filters.views import FilterView


class BlogListView(FilterView):
    model = BlogPost
    context_object_name = "blog"
    template_name = "blog/list.html"
    filterset_class = BlogFilter
