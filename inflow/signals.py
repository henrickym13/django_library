from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow


@receiver(post_save, sender=Inflow)
def update_book_quantity(sender, instance, **kwargs):
    if instance.quantity > 0:
        book = instance.book
        book.quantity += instance.quantity
        book.save()