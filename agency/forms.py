from django import forms
from .models import Tour, Service, Hotel, Excursion, OfficeEmployee


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'price', 'duration_days', 'photo', 'is_available', 'country', 'category']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'processing_days', 'is_active']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'stars', 'address', 'price_per_night', 'photo', 'country']


class ExcursionForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = ['title', 'description', 'duration_hours', 'price', 'photo', 'tours']


class OfficeEmployeeForm(forms.ModelForm):
    class Meta:
        model = OfficeEmployee
        fields = ['full_name', 'position', 'phone', 'email', 'photo']