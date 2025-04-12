from rest_framework import viewsets
from .models import Garage, Vehicle, Appointment
from .serializers import GarageSerializer, VehicleSerializer, AppointmentSerializer
from rest_framework.generics import ListAPIView
from appointments.models import Vehicle
from appointments.serializers import VehicleSerializer

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
