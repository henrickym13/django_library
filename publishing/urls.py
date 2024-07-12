from django.urls import path
from . import views


urlpatterns = [
    path('publishing/', views.PublishingListView.as_view(), name='publishing_list'),
    path('publishing/create/', views.PublishingCreateView.as_view(), name='publishing_create'),
    path('publishing/<int:pk>/detail/', views.PublishingDetailView.as_view(), name='publishing_detail'),
    path('publishing/<int:pk>/update/', views.PublishingUpdateView.as_view(), name='publishing_update'),
    path('publishing/<int:pk>/delete/', views.PublishingDeleteView.as_view(), name='publishing_delete')
]