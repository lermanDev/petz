from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from adopter.view import AdopterCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("registro/", AdopterCreateView.as_view(), name="registro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
