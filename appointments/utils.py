from datetime import datetime, timedelta
from .models import Appointment, Garage, Shift

from datetime import datetime, timedelta
from .models import Appointment

def generate_appointments_for_shift(shift):
    """
    برای یک شیفت مشخص، نوبت‌ها را بر اساس زمان شروع، پایان و فاصله بین نوبت‌ها ایجاد می‌کند.
    از ایجاد نوبت‌های تکراری جلوگیری می‌کند.
    """
    start = datetime.combine(shift.date, shift.start_time)
    end = datetime.combine(shift.date, shift.end_time)
    interval = timedelta(minutes=shift.interval_minutes)

    appointments = []
    current_time = start

    while current_time + interval <= end:
        exists = Appointment.objects.filter(
            garage=shift.garage,
            shift=shift,
            start_time=current_time
        ).exists()

        if not exists:
            appointments.append(Appointment(
                garage=shift.garage,
                shift=shift,
                start_time=current_time
            ))

        current_time += interval

    Appointment.objects.bulk_create(appointments)
    return appointments

