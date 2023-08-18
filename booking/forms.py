from django import forms
from .models import Booking, Table


class CheckAvailabilityForm(forms.Form):
    booking_date = forms.DateField()
    booking_time = forms.TimeField()
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'party_size', 'name', 'email', 'phone']

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
    }