from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GarageViewSet, VehicleViewSet, AppointmentViewSet

# ایجاد Router برای مدیریت API
router = DefaultRouter()
router.register(r'garages', GarageViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # همه APIهای ما در این مسیر خواهند بود
    
]
