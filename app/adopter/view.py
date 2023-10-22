from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Adopter
from .forms import AdopterRegistrationForm


class AdopterCreateView(CreateView):
    model = Adopter
    form_class = AdopterRegistrationForm
    template_name = "adopter_form.html"
    success_url = reverse_lazy("register")
