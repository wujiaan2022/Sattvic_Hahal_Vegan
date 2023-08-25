from django import forms
from .models import Booking, Table
from django.contrib import admin


TIME_CHOICES = [
    ('12:00 for Lunch', '12:00 Lunch Time'),
    ('18:00 for Dinner', '18:00 Dinner Time'),]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'name',
            'email',
            'phone',
            'time',
            'table',
            'date',
            'party_size',
        ]
        # widgets = {
        #    
        # }
       

class check_availability_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['time']
    

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    # fields = '__all__'
    fields = ['user', 'table', 'date', 'time', 'party_size', 'name', 'email', 'phone']
    

