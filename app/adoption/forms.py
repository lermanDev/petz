from django import forms
from .models import AdoptionApplication, Question, QuestionType, Option

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['user', 'pet', 'questionnaire']

    def __init__(self, *args, **kwargs):
        questionnaire = kwargs.pop('questionnaire')
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['pet'].widget = forms.HiddenInput()
        self.fields['questionnaire'].widget = forms.HiddenInput()
        
        for question in questionnaire.questions.all():
            field_name = f'question_{question.id}'
            if question.question_type == QuestionType.TEXT:
                self.fields[field_name] = forms.CharField(label=question.text, required=True)
            elif question.question_type == QuestionType.SELECT:
                choices = [(option.id, option.text) for option in question.options.all()]
                self.fields[field_name] = forms.ChoiceField(label=question.text, choices=choices, required=True)
            elif question.question_type == QuestionType.CHECKBOX:
                self.fields[field_name] = forms.BooleanField(label=question.text, required=False)

    def save(self, commit=True):
        application = super().save(commit=False)
        answers = {field_name.split('_')[1]: self.cleaned_data[field_name] for field_name in self.fields if field_name.startswith('question_')}
        application.answers = answers
        if commit:
            application.save()
        return application
