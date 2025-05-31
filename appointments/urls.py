from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentListView, GarageViewSet, VehicleViewSet, AppointmentViewSet, appointment_success, homepage, login_view, reserve_appointment, select_garage

# ایجاد Router برای مدیریت API
router = DefaultRouter()
router.register(r'garages', GarageViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # همه APIهای ما در این مسیر خواهند بود

     path('home', homepage, name='homepage'),
     path('select_garage/', select_garage, name='select_garage'),
    path('login/', login_view, name='login'),
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('reserve/<int:appointment_id>/', reserve_appointment, name='reserve_appointment'),
    path('success/', appointment_success, name='appointment_success'),


     
    
]
