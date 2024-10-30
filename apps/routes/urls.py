from django.urls import path
from .views import (
    RouteListView, RouteCreateView, RouteUpdateView, RouteDeleteView
)

urlpatterns = [
    path('', RouteListView.as_view(), name='route_list'),
    path('create/', RouteCreateView.as_view(), name='route_create'),
    path('update/<int:pk>/', RouteUpdateView.as_view(), name='route_update'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='route_delete'),
]
