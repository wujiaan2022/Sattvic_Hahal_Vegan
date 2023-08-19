from django.shortcuts import render
from .models import Booking, Table
# from .forms import BookingAdminForm, check_availability_form
from .forms import check_availability_form


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})


def show_available(request):
    if request.method == 'POST':
        form = check_availability_form(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            booked_tables = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_name', flat=True)
            max_table_number = 5 
            available_tables = [table_name for table_name in range(1, max_table_number + 1) if table_name not in booked_tables]
            return render(request, 'booking/show_available.html', {'available_tables': available_tables})
    else:
        return render(request, 'booking/show_available.html', {'available_tables': []})