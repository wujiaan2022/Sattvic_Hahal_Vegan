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
        
    # def __init__(self, *args, **kwargs):
    #     initial_data = kwargs.get('initial', {})
    #     initial_data.setdefault('time', '18:00 for Dinner')  # Set default time
    #     initial_data.setdefault('table', 'Table A1')  # Set default table
    #     initial_data.setdefault('date', '2023-12-25')  # Set default date
    #     kwargs['initial'] = initial_data
    #     super().__init__(*args, **kwargs)
       

class check_availability_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['time']
    

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    # fields = '__all__'
    fields = ['user', 'table', 'date', 'time', 'party_size', 'name', 'email', 'phone']
    

