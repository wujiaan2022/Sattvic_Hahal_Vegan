from django import forms
from .models import Booking, Table
from django.contrib import admin


COMMON_TIME_CHOICES = [
    ('12:00', 'Lunch Time'),
    ('18:00', 'Dinner Time'),
]


class check_availability_form(forms.Form):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    booking_time = forms.ChoiceField(choices=COMMON_TIME_CHOICES)
    

class BookingAdminForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = ['table', 'date', 'time', 'party_size', 'name', 'email', 'phone']
        fields = '__all__'
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.Select(choices=COMMON_TIME_CHOICES),
        
    }
    

