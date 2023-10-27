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
        base_template = (
            "partials/empty_base.html"
            if request.htmx
            else "registration/partials/base.html"
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                "registration/register.html",
                {
                    "form": form,
                    "registered": True,
                    "override_base_template": base_template,
                },
            )

        return render(
            request,
            "registration/register.html",
            {"form": form, "override_base_template": base_template},
        )


class AdopterLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"

    # def post(self, request):
    #     form = UserLoginForm(request, request.POST)
    #     base_template = (
    #         "partials/empty_base.html"
    #         if request.htmx
    #         else "registration/partials/base.html"
    #     )
    #     if form.is_valid():
    #         user = authenticate(
    #             username=form.cleaned_data["username"],
    #             password=form.cleaned_data["password"],
    #         )
    #         if user is not None:
    #             login(request, user)
    #             return render(
    #                 request,
    #                 "registration/login.html",
    #                 {
    #                     "form": form,
    #                     "override_base_template": base_template,
    #                     "logged": True,
    #                 },
    #             )

    #     return render(
    #         request,
    #         "registration/login.html",
    #         {"form": form, "override_base_template": base_template},
    #     )
