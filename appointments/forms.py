from django import forms
from .models import Customer, Vehicle

class AppointmentForm(forms.Form):
    first_name = forms.CharField(label="نام", max_length=50)
    last_name = forms.CharField(label="نام خانوادگی", max_length=50)
    mobile = forms.CharField(label="شماره موبایل", max_length=11)

    plate_first = forms.CharField(label="پلاک اول", max_length=2)
    plate_letter = forms.CharField(label="حرف پلاک", max_length=1)
    plate_second = forms.CharField(label="پلاک دوم", max_length=3)
    plate_city = forms.CharField(label="کد شهر", max_length=2)

    color = forms.CharField(label="رنگ خودرو", max_length=30)
    brand = forms.CharField(label="برند خودرو", max_length=50)
    year = forms.IntegerField(label="سال ساخت")
    issue = forms.CharField(label="مشکل خودرو", widget=forms.Textarea)
