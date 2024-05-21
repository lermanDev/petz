from django.contrib import admin
from django import forms
from .models import AdoptionApplication, Question, Option, Questionnaire, QuestionType


class OptionAdminForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = '__all__'

    question = forms.ModelChoiceField(
        queryset=Question.objects.filter(question_type=QuestionType.SELECT),
        label="Question",
        help_text="Select a checkbox question."
    )

class OptionAdmin(admin.ModelAdmin):
    form = OptionAdminForm


admin.site.register(AdoptionApplication)
admin.site.register(Question)
admin.site.register(Questionnaire)

admin.site.register(Option, OptionAdmin)