from django import forms
from . import models


class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields= ['title', 'category', 'publishing', 'supplier', 'author', 'isbn_10', 
            'isbn_13', 'cost_price', 'selling_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'publishing': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'isbn_10': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn_13': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category' : 'Gênero',
            'publishing': 'Editora',
            'supplier': 'Fornecedor',
            'author': 'Autor',
            'isbn_10': 'ISBN 10',
            'isbn_13': 'ISBN 13',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
        }