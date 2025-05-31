from rest_framework import viewsets
from django.shortcuts import redirect, render, get_object_or_404
from .models import Garage, Vehicle, Appointment
from .serializers import GarageSerializer, VehicleSerializer, AppointmentSerializer
from django.views import View




def homepage(request):
    garages = Garage.objects.all()
    return render(request, 'appointments/home.html', {'garages': garages})


def select_garage(request):
    garage_id = request.GET.get('garage_id')
    if not garage_id:
        return render(request, 'appointments/error.html', {'message': 'تعمیرگاه انتخاب نشده'})

    garage = get_object_or_404(Garage, id=garage_id)
    appointments = Appointment.objects.filter(garage=garage)

    return render(request, 'appointments/appointment_list.html', {
        'garage': garage,
        'appointments': appointments,
    })

def login_view(request):
    return render(request, 'appointments/login.html')

# ویوست برای تعمیرگاه‌ها
class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

# ویوست برای خودروها
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# ویوست برای نوبت‌ها
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

from django.views.generic import ListView
from .models import Appointment, Garage
from django.shortcuts import get_object_or_404

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        garage_id = self.request.GET.get('garage_id')
        self.garage = get_object_or_404(Garage, id=garage_id)
        return Appointment.objects.filter(garage=self.garage, status='pending')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['garage'] = self.garage
        return context

def reserve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        # فرض می‌کنیم رزرو انجام شده
        appointment.status = 'pending'  # یا مثلاً 'reserved' اگر بخوای وضعیت جدید داشته باشی
        appointment.save()
        return redirect('appointment_success')  # بعداً اینو تعریف می‌کنی

    return render(request, 'appointments/reserve.html', {'appointment': appointment})



def appointment_success(request):
    return render(request, 'appointments/success.html')
