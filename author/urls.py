from django.urls import path
from . import views


urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/detail/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete')
]