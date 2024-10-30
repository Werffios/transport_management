from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Vehicle

class VehicleListView(generic.ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleCreateView(generic.CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(generic.UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(generic.DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')
