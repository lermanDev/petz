from django import forms
from .models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = [
            "pet",
            "user",
            "shelter",
            "adopted_by",
            "status",
            "extra_location",
            "entry_date",
            "description",
        ]
