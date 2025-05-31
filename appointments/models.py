from django.db import models

class Garage(models.Model):  # مدل تعمیرگاه
    name = models.CharField(max_length=255)  # نام تعمیرگاه
    address = models.CharField(max_length=255, blank=True)  # آدرس
    phone_number = models.CharField(max_length=15, blank=True)  # شماره تماس
    description = models.TextField(blank=True)  # توضیحات
    max_appointments_per_day = models.IntegerField(default=10)  # حداکثر نوبت‌ها در روز
    appointment_interval = models.PositiveIntegerField(default=15)  # فاصله زمانی نوبت‌ها (دقیقه)
    open_from = models.TimeField(null=True, blank=True)  # ساعت شروع کار
    open_until = models.TimeField(null=True, blank=True)  # ساعت پایان کار
    appointments_per_morning = models.IntegerField(default=5)  # نوبت‌های صبح
    appointments_per_afternoon = models.IntegerField(default=5)  # نوبت‌های عصر

    def __str__(self):
        return self.name


class User(models.Model):  # مدل کاربر
    first_name = models.CharField(max_length=50)  # نام
    last_name = models.CharField(max_length=50)  # نام خانوادگی
    mobile_number = models.CharField(max_length=15, unique=True)  # شماره موبایل (یکتا)
    verification_code = models.CharField(max_length=6, null=True, blank=True)  # کد تأیید
    is_active = models.BooleanField(default=False)  # وضعیت فعال بودن
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ثبت‌نام
    updated_at = models.DateTimeField(auto_now=True)  # آخرین تغییر

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_number}"



class Vehicle(models.Model):
    # انتخاب رنگ از لیست رنگ‌های پرکاربرد
    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
        ('gray', 'Gray'),
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('silver', 'Silver'),
        ('orange', 'Orange'),
        ('brown', 'Brown'),
        
    ]

    license_plate_part1 = models.CharField(max_length=5, blank=True, null=True)  # اولین قسمت پلاک
    license_plate_part2 = models.CharField(max_length=5, blank=True, null=True)  # دومین قسمت پلاک
    license_plate_part3 = models.CharField(max_length=5, blank=True, null=True)  # سومین قسمت پلاک
    license_plate_part4 = models.CharField(max_length=5, blank=True, null=True)  # چهارمین قسمت پلاک

    color = models.CharField(max_length=20, choices=COLOR_CHOICES)  # رنگ خودرو از لیست انتخابی
    brand = models.CharField(max_length=50)  # برند خودرو
    year = models.PositiveIntegerField()  # سال ساخت
    issue = models.TextField()  # مشکل خودرو
    owner = models.ForeignKey('User', on_delete=models.CASCADE)  # صاحب خودرو

    def get_license_plate(self):
        """ساخت پلاک کامل خودرو"""
        return f"{self.license_plate_part1} {self.license_plate_part2} {self.license_plate_part3} {self.license_plate_part4}"

    def __str__(self):
        # نمایش پلاک به صورت کامل
        return f"{self.license_plate_part1} {self.license_plate_part2} {self.license_plate_part3} {self.license_plate_part4} - {self.color}"



class Appointment(models.Model):  # مدل نوبت‌دهی
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)  # تعمیرگاه
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)  # خودرو
    appointment_date = models.DateTimeField()  # زمان نوبت
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed')], 
        default='pending'  # مقدار پیش‌فرض
    )

    def __str__(self):
        return f"Appointment for {self.vehicle} at {self.appointment_date}"
    


class Shift(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    date = models.DateField()  # تاریخ شمسی ذخیره شده به صورت میلادی
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.garage.name} - {self.date} | {self.start_time} to {self.end_time}"

