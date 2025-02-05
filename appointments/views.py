from rest_framework import viewsets
from .models import Garage
from .serializers import GarageSerializer

class GarageViewSet(viewsets.ModelViewSet):
    """
    ViewSet برای مدیریت تعمیرگاه‌ها (CRUD کامل)
    """
    queryset = Garage.objects.all()  # دریافت تمام تعمیرگاه‌ها
    serializer_class = GarageSerializer  # استفاده از سریالایزر مربوطه
