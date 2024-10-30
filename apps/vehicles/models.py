from django.db import models
from apps.routes.models import Route

# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('BUS', 'Bus'),
        ('TRUCK', 'Camión'),
        ('CAR', 'Automóvil'),
        ('SUV', 'SUV'),
    ]

    plate_number = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPE_CHOICES)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.plate_number