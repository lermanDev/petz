from django import forms
from .models import AdoptionRequest


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


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ["pet", "message"]

        widgets = {
            "pet": forms.Select(),
            "message": forms.Textarea(attrs={"rows": 4}),
        }
