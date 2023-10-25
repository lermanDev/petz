from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Adopter
from .forms import AdopterRegistrationForm


class AdopterCreateView(CreateView):
    model = Adopter
    form_class = AdopterRegistrationForm
    template_name = "adopter/register.html"
    success_url = reverse_lazy("register")

    def post(self, request):
        form = AdopterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "adopter/partials/registration_complete.html")

        return render(
            request, "adopter/partials/registration_form.html", {"form": form}
        )
