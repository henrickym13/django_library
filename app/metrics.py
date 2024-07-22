from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from book.models import Book


def get_book_metrics():
    books = Book.objects.all()
    total_cost_price = sum(book.cost_price * book.quantity for book in books)
    total_selling_price = sum(book.selling_price * book.quantity for book in books)
    total_quantity = sum(book.quantity for book in books)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )