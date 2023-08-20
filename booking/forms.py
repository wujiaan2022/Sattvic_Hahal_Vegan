from django import forms
from .models import Booking, Table
from django.contrib import admin


TIME_CHOICES = [
    ('12:00 for Lunch', '12:00 Lunch Time'),
    ('18:00 for Dinner', '18:00 Dinner Time'),]


class BookingForm(forms.Form):    
    
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'id': 'booking-time', 'style': 'display:none;'})
    )
    table = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'booking-table'}))
    date = forms.DateField(widget=forms.HiddenInput(attrs={'id': 'booking-date'}))


class check_availability_form(forms.Form):
    # booking_date = forms.DateField(
    #     # widget=forms.DateInput(attrs={'type': 'date',})
    # )
    time = forms.ChoiceField(choices=TIME_CHOICES)
    

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    # fields = '__all__'
    fields = ['table', 'date', 'time', 'party_size', 'name', 'email', 'phone']
    

