from django.urls import path
from .views import AssignVehicleView, AssignmentLogListView, AssignmentSuccessView

urlpatterns = [
    path('assign/', AssignVehicleView.as_view(), name='assign_vehicle'),
    path('logs/', AssignmentLogListView.as_view(), name='assignment_logs'),
    path('success/', AssignmentSuccessView.as_view(), name='assignment_success'),
]
