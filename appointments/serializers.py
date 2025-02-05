from rest_framework import serializers
from .models import Garage, Appointment, Vehicle, User

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'  # همه فیلدها را در JSON نمایش بده
