from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from adopter.view import AdopterCreateView, AdopterLoginView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", AdopterCreateView.as_view(), name="register"),
    path("login/", AdopterLoginView.as_view(), name="login"),
    # path("adopter/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
