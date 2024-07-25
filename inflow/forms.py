from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'book', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'book': 'Livro',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }