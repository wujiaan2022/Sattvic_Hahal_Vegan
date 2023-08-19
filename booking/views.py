from django.shortcuts import render
from .models import Booking, Table
from .forms import check_availability_form


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})

    
def show_available(request):
    booking_date = request.GET.get('date')
    booking_time = request.GET.get('time')
    
    if booking_date and booking_time:
        booked_tables = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table', flat=True)
        max_table_number = 5 
        available_tables = [table for table in range(1, max_table_number + 1) if table not in booked_tables]
        
        return render(request, 'booking/show_available.html', {'available_tables': available_tables})
    else:
        # Handle the case when no valid form data is provided
        return render(request, 'booking/show_available.html', {'available_tables': []})