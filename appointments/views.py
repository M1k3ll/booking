from rest_framework import viewsets
from django.shortcuts import redirect, render, get_object_or_404
from .models import Garage, Vehicle, Appointment
from .serializers import GarageSerializer, VehicleSerializer, AppointmentSerializer
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Shift, Appointment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer


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





def available_appointments_view(request, shift_id):
    # شیفتی که کاربر انتخاب کرده بر اساس id از دیتابیس گرفته می‌شود
    shift = get_object_or_404(Shift, id=shift_id)

    # فقط نوبت‌هایی که هنوز رزرو نشده‌اند را فیلتر می‌کنیم
    appointments = Appointment.objects.filter(
        shift=shift,          # مربوط به همین شیفت
        is_reserved=False     # فقط نوبت‌هایی که هنوز رزرو نشده‌اند
    ).order_by('start_time')  # به ترتیب زمانی

    # نمایش صفحه HTML و ارسال شیفت و لیست نوبت‌ها به قالب
    return render(request, 'appointments/available_appointments.html', {
        'shift': shift,
        'appointments': appointments
    })



@api_view(['GET'])  # فقط درخواست GET اجازه دارد این ویو را صدا بزند
def available_appointments_api(request, shift_id):
    # فقط نوبت‌هایی را می‌گیریم که برای این شیفت و آزاد (رزرو نشده) هستند
    appointments = Appointment.objects.filter(
        shift_id=shift_id,
        is_reserved=False
    ).order_by('start_time')  # مرتب‌سازی بر اساس زمان شروع

    # سریالایز کردن نوبت‌ها به JSON
    serializer = AppointmentSerializer(appointments, many=True)

    # برگرداندن پاسخ JSON
    return Response(serializer.data)