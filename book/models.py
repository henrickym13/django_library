from django.db import models
from category.models import Category
from supplier.models import Supplier
from publishing.models import Publishing
from author.models import Author


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    publishing = models.ForeignKey(Publishing, on_delete=models.PROTECT, related_name='books')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    isbn_10 = models.CharField(max_length=10, unique=True)
    isbn_13 = models.CharField(max_length=20, unique=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title