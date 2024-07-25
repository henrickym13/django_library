from django.urls import path
from . import views


urlpatterns = [
    path('inflow/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflow/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflow/<int:pk>/detail/',views.InflowDetailView.as_view(), name='inflow_detail')
]