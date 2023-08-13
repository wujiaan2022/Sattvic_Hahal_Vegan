from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'party_size', 'name', 'email', 'phone']

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
    }