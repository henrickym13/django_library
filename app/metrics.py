from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from book.models import Book
from category.models import Category
from publishing.models import Publishing
from outflow.models import Outflow


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


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_books_sold = Outflow.objects.aggregate(total_books_sold=Sum('quantity'))['total_books_sold'] or 0
    total_sales_value = sum(outflow.quantity * outflow.book.selling_price for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.quantity * outflow.book.cost_price for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales = total_sales,
        total_books_sold = total_books_sold,
        total_sales_value = number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit = number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('book__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))
    
    return dict(
        dates = dates,
        values = values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)
    
    return dict(
        dates = dates,
        values = quantities,
    )


def get_graphic_book_category_metric():
    categories = Category.objects.all()
    return {category.name: Book.objects.filter(category=category).count() for category in categories}


def get_graphic_book_publishing_metric():
    publishies = Publishing.objects.all()
    return {publishing.name: Book.objects.filter(publishing=publishing).count() for publishing in publishies}
