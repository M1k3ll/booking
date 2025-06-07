from datetime import datetime, timedelta
from .models import Appointment, Garage, Shift

def generate_appointments_for_shift(shift):
    """
    برای یک شیفت مشخص نوبت‌ها را بر اساس زمان شروع، پایان و فاصله تعیین می‌کند.
    """
    start = datetime.combine(shift.date, shift.start_time)
    end = datetime.combine(shift.date, shift.end_time)
    interval = timedelta(minutes=shift.garage.appointment_interval)

    appointments = []
    current = start
    while current + interval <= end:
        if not Appointment.objects.filter(garage=Garage, shift=shift, start_time=current_time).exists():
            Appointment.objects.create(
                garage=Garage,
                shift=shift,
                start_time=current_time
            )
        current_time += interval
    Appointment.objects.bulk_create(appointments)
    return appointments
