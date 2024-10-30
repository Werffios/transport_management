from django import forms
from apps.vehicles.models import Vehicle
from apps.routes.models import Route

class VehicleAssignmentForm(forms.Form):
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.filter(route__isnull=True),
        label='Vehicle'
    )
    route = forms.ModelChoiceField(
        queryset=Route.objects.all(),
        label='Route'
    )
