from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", include("adoption.urls")),
    path("weblog/", include("zinnia.urls")),
    path("comments/", include("django_comments.urls")),
]
