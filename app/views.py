from django.shortcuts import render
from . import metrics
import json


def index(request):
    book_metrics = metrics.get_book_metrics()
    sales_metrics = metrics.get_sales_metrics()
    graphic_book_category_metric = metrics.get_graphic_book_category_metric()
    graphic_book_publishing_metric = metrics.get_graphic_book_publishing_metric()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()

    context = {
        'book_metrics': book_metrics,
        'sales_metrics': sales_metrics,
        'book_count_by_category': json.dumps(graphic_book_category_metric),
        'book_count_by_publishing': json.dumps(graphic_book_publishing_metric),
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data)
    }
    
    return render(request, 'index.html', context)