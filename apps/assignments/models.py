from django.db import models

# Create your models here.
class AssignmentLog(models.Model):
    vehicle_plate = models.CharField(max_length=10)
    route_name = models.CharField(max_length=100)
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_plate} assigned to {self.route_name}"