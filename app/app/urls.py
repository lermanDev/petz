from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from adopter.view import AdopterCreateView, AdopterLoginView
from pet.view import PetListView, PetView
from blog.view import BlogListView, BlogPostDetailView
from shelter.view import ShelterListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", AdopterCreateView.as_view(), name="register"),
    path("login", AdopterLoginView.as_view(next_page="login"), name="login"),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("blog", BlogListView.as_view(), name="blog"),
    path('blog/<str:slug>', BlogPostDetailView.as_view(), name='blog_detail'),  # Using slug
    path('shelters/', ShelterListView.as_view(), name='shelters'),
    path("", PetListView.as_view(), name="pets"),
    path(
        "adopt/<str:specie>/<str:city>/<str:id>_<str:name>",
        PetView.as_view(),
        name="pet",
    )
    # path("adopter/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
