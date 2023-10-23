from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={"placeholder": "Search..."})
    )
