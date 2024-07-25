from django.db import models
from book.models import Book
from supplier.models import Supplier


# Create your models here.
class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.book)