from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Adopter
from .forms import AdopterRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect


class AdopterCreateView(CreateView):
    model = Adopter
    form_class = AdopterRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def post(self, request):
        form = AdopterRegistrationForm(request.POST)
        base_template = (
            "partials/empty_base.html"
            if request.htmx
            else "registration/partials/base.html"
        )
        if form.is_valid():
            form.save()
            return reverse_lazy("login")

        return render(
            request,
            "registration/register.html",
            {"form": form, "override_base_template": base_template},
        )


class AdopterLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("login")
