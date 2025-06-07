# appointment/apps.py
from django.apps import AppConfig

class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    def ready(self):
        import appointment.signals  # 👈 سیگنال‌ها رو در لحظه شروع اپ لود کن
