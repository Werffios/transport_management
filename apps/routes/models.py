from django.db import models

# Create your models here.
class Route(models.Model):
    ROUTE_TYPE_CHOICES = [
        ('PAVEMENT', 'Pavimento'),
        ('POTHOLES', 'Pavimento con Baches'),
        ('DIRT', 'Camino de Tierra'),
        ('TRAIL', 'Sendero'),
    ]

    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    route_type = models.CharField(max_length=10, choices=ROUTE_TYPE_CHOICES)

    def __str__(self):
        return self.name