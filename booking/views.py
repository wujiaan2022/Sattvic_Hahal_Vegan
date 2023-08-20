from django.shortcuts import render
from .models import Booking, Table
from .forms import check_availability_form


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})

    
def show_available(request):
    booking_date = request.GET.get('date')  # Get booking_date from your request data
    booking_time = request.GET.get('time')  # Get booking_time from your request data

    if booking_date and booking_time:
        booked_table_numbers = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_id', flat=True)
     
        available_tables = Table.objects.exclude(id__in=booked_table_numbers)
    
        return render(request, 'booking/show_available.html', {'available_tables': available_tables})
    
    else:
        return render(request, 'booking/show_available.html', {'available_tables': []})

    
    
    # def show_available(request):
    #     booking_date = request.GET.get('date')  # Get booking_date from your request data
    #     booking_time = request.GET.get('time') # Get booking_time from your request data

    #     if booking_date and booking_time:
    #         booked_table_numbers = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_id', flat=True)
        
    #         available_table_numbers = [table.id for table in Table.objects.all() if table.id not in booked_table_numbers]
        
    #         return render(request, 'booking/show_available.html', {'available_table_numbers': available_table_numbers})
    
    #     else:
    #         return render(request, 'booking/show_available.html', {'available_table_numbers': []})
