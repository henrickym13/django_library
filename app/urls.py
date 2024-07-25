from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('supplier.urls')),
    path('', include('publishing.urls')),
    path('', include('category.urls')),
    path('', include('author.urls')),
    path('', include('book.urls')),
    path('', include('inflow.urls')),
]
