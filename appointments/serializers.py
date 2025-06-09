from rest_framework import serializers
from .models import Garage, Vehicle, Appointment

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    # Serializer برای تبدیل مدل Appointment به JSON و بالعکس
    class Meta:
        model = Appointment
        fields = ['id', 'shift', 'garage', 'start_time', 'is_reserved']
        # این فیلدها در خروجی JSON نمایش داده می‌شوند