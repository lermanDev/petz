from .filters import BlogFilter
from .models import BlogPost
from django_filters.views import FilterView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView



class BlogListView(FilterView):
    model = BlogPost
    context_object_name = "blog"
    template_name = "blog/blog.html"
    filterset_class = BlogFilter

    def get(self, request):
        filter = BlogFilter(request.GET, queryset=BlogPost.objects.all())
        paginator = Paginator(filter.qs, 15)
        page = request.GET.get("page")
        try:
            blog_paginated = paginator.page(page)
        except PageNotAnInteger:
            blog_paginated = paginator.page(1)
        except EmptyPage:
            blog_paginated = paginator.page(paginator.num_pages)

        # Determining if filtering is applied
        is_filtering = any(1 for key, value in request.GET.items() if key != 'page' and (value or value==''))

        # Determining if pagination is applied
        is_paginating = page is not None

        context = {"blog_list": blog_paginated, "filter": filter, "extends_base": "base.html"}

        if request.htmx:
            context["extends_base"] = "partials/empty_base.html"

        if (is_filtering or is_paginating) and request.htmx:
            return render(
                request,
                "blog/partials/list.html",
                context,
            )
        
        return render(
            request,
            "blog/blog.html",
            context,
        )

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'  # This variable will be used in the template

    def get(self, request, *args, **kwargs):
        blog = BlogPost.objects.get(slug=kwargs["slug"])
        filter = BlogFilter(request.GET, queryset=BlogPost.objects.all())

        context = {"blog": blog, "filter": filter}
        if request.htmx:
            return render(
                request,
                "blog/partials/detail.html",
                context,
            )

        return render(
            request,
            "blog/blog_detail.html",
            context,
        )
