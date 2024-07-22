from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/detail', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]