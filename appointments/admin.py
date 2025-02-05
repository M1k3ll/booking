from django.contrib import admin
from .models import Garage, Appointment, User, Vehicle

# # نمایش خودروهای یک کاربر در پنل ادمین
# class VehicleInline(admin.TabularInline):
#     model = Vehicle
#     extra = 1  # تعداد فرم‌های خالی برای اضافه کردن خودرو
#     fields = ('license_plate', 'brand', 'color', 'year')  # فیلدهایی که نمایش داده می‌شوند

# @admin.register(Garage)
# class GarageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'description', 'open_from', 'appointments_per_morning', 'appointments_per_afternoon')  
#     search_fields = ('name', 'address', 'description')  
#     list_filter = ('open_from', 'appointments_per_morning', 'appointments_per_afternoon')  
#     list_editable = ('address', 'description', 'open_from', 'appointments_per_morning', 'appointments_per_afternoon')  

# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('garage', 'vehicle', 'appointment_date', 'status')  
#     search_fields = ('garage__name', 'vehicle__license_plate')  
#     list_filter = ('status', 'appointment_date')  
#     list_editable = ('status',)  

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'mobile_number', 'is_active', 'created_at')  
#     search_fields = ('first_name', 'last_name', 'mobile_number')  
#     list_filter = ('is_active', 'created_at')  
#     list_editable = ('is_active',)  
#     inlines = [VehicleInline]  # نمایش خودروها در داخل فرم کاربر

# @admin.register(Vehicle)
# class VehicleAdmin(admin.ModelAdmin):
#     list_display = ('license_plate', 'brand', 'color', 'year', 'owner')  
#     search_fields = ('license_plate', 'brand', 'owner__first_name', 'owner__last_name')  
#     list_filter = ('brand', 'color', 'year')  
#     list_editable = ('brand', 'color', 'year')  




# مدل تعمیرگاه
@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'description', 'max_appointments_per_day', 'appointment_interval', 'open_from', 'open_until', 'appointments_per_morning', 'appointments_per_afternoon')  # نمایش فیلدها در لیست
    search_fields = ('name', 'address', 'phone_number')  # جستجو بر اساس این فیلدها
    list_filter = ('name',)  # فیلتر بر اساس نام تعمیرگاه

# مدل نوبت
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('garage', 'vehicle', 'appointment_date', 'status')  # نمایش فیلدها در لیست
    search_fields = ('garage__name', 'vehicle__license_plate')  # جستجو بر اساس تعمیرگاه و پلاک خودرو
    list_filter = ('status', 'appointment_date')  # فیلتر بر اساس وضعیت و تاریخ

# مدل کاربر
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'is_active')  # نمایش فیلدها در لیست
    search_fields = ('first_name', 'last_name', 'mobile_number')  # جستجو بر اساس نام و شماره موبایل
    list_filter = ('is_active',)  # فیلتر بر اساس وضعیت فعال بودن


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('get_license_plate', 'color', 'brand', 'year', 'owner')  # نمایش پلاک کامل و فیلدهای دیگر
    search_fields = ('license_plate_part1', 'license_plate_part2', 'license_plate_part3', 'license_plate_part4', 'brand', 'owner__first_name')  # جستجو بر اساس قسمت‌های پلاک و سایر فیلدها
    list_filter = ('color', 'brand')  # فیلتر بر اساس رنگ و برند
