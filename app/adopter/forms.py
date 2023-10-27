from django import forms
from .models import Adopter
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AdopterRegistrationForm(UserCreationForm):
    class Meta:
        model = Adopter
        fields = [
            "username",
            "email",
        ]


class UserLoginForm(AuthenticationForm):
    pass
