from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Booking, Table
from .forms import check_availability_form, BookingForm
from datetime import datetime


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})

    
def show_available(request):
        
    booking_date = request.GET.get('date')  
    booking_time = request.GET.get('time') 

    available_tables = []

    if booking_date and booking_time:
        booked_table_numbers = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_id', flat=True)
        available_tables = Table.objects.exclude(id__in=booked_table_numbers)
        
    return render(request, 'booking/show_available.html', {
                'available_tables': available_tables,
                
                'booking_date': booking_date,
                'booking_time': booking_time,
                }) 
  

def booking_form(request, table_id, booking_date, booking_time):
    
    table = Table.objects.get(id=table_id)
#   
    
    if request.user.is_authenticated:
        user = request.user
        initial_data = {'name': user.username, 'email': user.email}
    # else:
    #     initial_data = {}

    if request.method == 'POST':
        print("Form submitted!")
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.date = booking_date
            booking.time = booking_time
            
            try:
                booking.save()
                print('Booking successful.')
            except Exception as e:
                print("Error while saving booking:", e)
                
            return redirect('home', table_id=table.id, booking_date=booking_date, booking_time=booking_time)
        else:
            print("Form is NOT valid:", form.errors.as_data())
    else:
        form = BookingForm(initial=initial_data)
    
    return render(request, 'booking/booking_form.html', 
                  {'table': table, 'form': form, 'booking_date': booking_date, 'booking_time': booking_time})



def booking_confirmation(request, table_id, booking_date, booking_time):
    table = Table.objects.get(id=table_id)
    booking = {
        'table': table,
        'date': booking_date,
        'time': booking_time,
        # Add other booking information here
    }
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})        