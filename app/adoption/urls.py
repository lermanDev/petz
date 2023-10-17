from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    # path("pets/", views.hello_world, name="pets"),
    path("", views.hello_world, name="hello_world"),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
