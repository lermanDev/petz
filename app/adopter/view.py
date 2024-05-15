from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Adopter
from .forms import AdopterRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate


class AdopterCreateView(CreateView):
    model = Adopter
    form_class = AdopterRegistrationForm
    template_name = "registration/register.html"

    def post(self, request):
        form = AdopterRegistrationForm(request.POST)
        context = {"form": form}
        template_name = "registration/register.html"

        if request.htmx:
            template_name = "registration/partials/registration_form.html"

        if form.is_valid():
            form.save()
            if request.htmx:
                template_name = "registration/partials/registration_success.html"
            context["registered"] = True

        return render(
            request,
            template_name,
            context,
        )


class AdopterLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"

    def get(self, request):
        form = UserLoginForm()
        context = {"form": form, "extends_base": "base.html"}
        template_name = "registration/login.html"

        if request.htmx:
            context["extends_base"] = "partials/empty_base.html"

        return render(
            request,
            template_name,
            context,
        )