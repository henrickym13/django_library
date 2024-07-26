from django.db import models
from book.models import Book


# Create your models here.
class Outflow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.book)