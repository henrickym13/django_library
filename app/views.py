from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import metrics
import json


def login_user(request):
    if request.user.is_authenticated:
        return render('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')