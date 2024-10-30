from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Route

class RouteListView(generic.ListView):
    model = Route
    template_name = 'routes/route_list.html'
    context_object_name = 'routes'

class RouteCreateView(generic.CreateView):
    model = Route
    fields = '__all__'
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')

class RouteUpdateView(generic.UpdateView):
    model = Route
    fields = '__all__'
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')

class RouteDeleteView(generic.DeleteView):
    model = Route
    template_name = 'routes/route_confirm_delete.html'
    success_url = reverse_lazy('route_list')
