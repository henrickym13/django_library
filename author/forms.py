from django import forms
from . import models


class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = ['name',]
        widgets = {
            'name': forms.TimeInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
        }