from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GarageViewSet

# ایجاد یک Router برای API
router = DefaultRouter()
router.register(r'garages', GarageViewSet)  # ثبت مسیر API برای تعمیرگاه‌ها

urlpatterns = [
    path('api/', include(router.urls)),  # اضافه کردن مسیرهای API به پروژه
]
