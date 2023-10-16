from django.urls import path
from . import views

urlpatterns = [
    # path("pets/", views.hello_world, name="pets"),
    path("", views.hello_world, name="hello_world"),
]
