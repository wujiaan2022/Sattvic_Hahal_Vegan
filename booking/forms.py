from django import forms
from .models import Booking, Table
from django.contrib import admin


TIME_CHOICES = [
    ('12:00 for Lunch', 'Lunch Time'),
    ('18:00 for Dinner', 'Dinner Time'),]


class check_availability_form(forms.Form):
    # booking_date = forms.DateField(
    #     # widget=forms.DateInput(attrs={'type': 'date',})
    # )
    time = forms.ChoiceField(choices=TIME_CHOICES)
    

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    # fields = '__all__'
    fields = ['table', 'date', 'time', 'party_size', 'name', 'email', 'phone']
    

