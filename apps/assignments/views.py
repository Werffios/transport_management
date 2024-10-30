from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View, generic
from .forms import VehicleAssignmentForm
from .models import AssignmentLog
from apps.vehicles.models import Vehicle
from apps.routes.models import Route

class AssignVehicleView(View):
    def get(self, request):
        form = VehicleAssignmentForm()
        return render(request, 'assignments/assign_vehicle.html', {'form': form})

    def post(self, request):
        form = VehicleAssignmentForm(request.POST)
        if form.is_valid():
            vehicle = form.cleaned_data['vehicle']
            route = form.cleaned_data['route']
            if self.is_valid_assignment(vehicle, route):
                vehicle.route = route
                vehicle.save()
                AssignmentLog.objects.create(
                    vehicle_plate=vehicle.plate_number,
                    route_name=route.name
                )
                return redirect('assignment_success')
            else:
                form.add_error(None, 'Vehicle type does not match route type.')
        return render(request, 'assignments/assign_vehicle.html', {'form': form})

    def is_valid_assignment(self, vehicle, route):
        assignment_rules = {
            'PAVEMENT': 'BUS',
            'POTHOLES': 'TRUCK',
            'DIRT': 'CAR',
            'TRAIL': 'SUV',
        }
        return assignment_rules.get(route.route_type) == vehicle.vehicle_type

class AssignmentLogListView(generic.ListView):
    model = AssignmentLog
    template_name = 'assignments/assignment_log_list.html'
    context_object_name = 'logs'

    def get_queryset(self):
        queryset = super().get_queryset()
        plate_number = self.request.GET.get('plate_number')
        if plate_number:
            queryset = queryset.filter(vehicle_plate=plate_number)
        return queryset

class AssignmentSuccessView(generic.TemplateView):
    template_name = 'assignments/assignment_success.html'
