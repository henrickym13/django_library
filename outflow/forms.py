from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):
    
    class Meta:
        model = models.Outflow
        fields = ['book', 'quantity', 'description']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'book': 'Livro',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        book = self.cleaned_data.get('book')

        if quantity > book.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o livro {book.title} é de {book.quantity} unidades.'  
            )
        
        return quantity