from django.urls import path
from .views import (
    VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView
)

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
    path('create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle_delete'),
]
