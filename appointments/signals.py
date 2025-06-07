# appointment/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shift
from .utils import generate_appointments_for_shift

@receiver(post_save, sender=Shift)
def create_appointments_after_shift_save(sender, instance, created, **kwargs):
    """
    وقتی شیفت جدید ساخته شد، بلافاصله نوبت‌های آن نیز تولید می‌شود.
    """
    if created:
        generate_appointments_for_shift(instance)
