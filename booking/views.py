from django.shortcuts import render
from .models import Booking, Table
from .forms import BookingAdminForm, check_availability_form


def check_availability(request):
    if request.method == 'POST':
        form = check_availability_form(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            booked_tables = Booking.objects.filter(date=booking_date, time__lte=booking_time).values_list('table_number', flat=True)
            max_table_number = 5 
            available_tables = [table_number for table_number in range(1, max_table_number + 1) if table_number not in booked_tables]
            return render(request, 'booking/availability_result.html', {'available_tables': available_tables})
    else:
        form = check_availability_form()
    return render(request, 'booking/booking.html', {'form': form})

