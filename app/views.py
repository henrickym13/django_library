from django.shortcuts import render
from . import metrics


def index(request):
    book_metrics = metrics.get_book_metrics()

    context = {
        'book_metrics': book_metrics
    }

    return render(request, 'index.html', context)