from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
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
        booked_table = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_id', flat=True)
        available_tables = Table.objects.exclude(id__in=booked_table)
        
    return render(request, 'booking/show_available.html', {
                'available_tables': available_tables,                
                'booking_date': booking_date,
                'booking_time': booking_time,
                }) 
  

def booking_form(request, table_id, booking_date, booking_time):
    table = Table.objects.get(id=table_id)
    initial_data = {'table': table, 'date': booking_date, 'time': booking_time}

    if request.user.is_authenticated:
        initial_data['name'] = request.user.username
        initial_data['email'] = request.user.email        
        
        if request.method == 'POST':
            form = BookingForm(request.POST)
            
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.date = booking_date
                booking.time = booking_time
                booking.name = request.user.username                 
                
                try:
                    booking.save()
                    print('Booking successful.')
                except Exception as e:
                    print("Error while saving booking:", e)
                
                return redirect('booking_confirmation', table_id=table.id, booking_date=booking_date, booking_time=booking_time,
                                name=request.user.username, email=request.user.email)
            else:
                print("Form is NOT valid:", form.errors.as_data())
        else:
            form = BookingForm(initial=initial_data)
    else:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.date = booking_date
                booking.time = booking_time
                booking.name = form.cleaned_data['name']
                booking.email = form.cleaned_data['email']  
                booking.phone = form.cleaned_data['phone']    
                
                try:
                    booking.save()
                    print('Booking successful.')
                except Exception as e:
                    print("Error while saving booking:", e)
                
                return redirect('booking_confirmation', table_id=table.id, booking_date=booking_date, booking_time=booking_time,
                                name=booking.name, email=booking.email, phone=booking.phone)
    
    return render(request, 'booking/booking_form.html', {'form': form, 'table': table, 'booking_date': booking_date, 'booking_time': booking_time})


    


def booking_confirmation(request, table_id, booking_date, booking_time):
    if request.method == 'POST':
        table = Table.objects.get(id=table_id)
        name = request.POST.get('name')  # Retrieve name from the form
        email = request.POST.get('email')  # Retrieve email from the form
        phone = request.POST.get('phone')  # Retrieve phone from the form

        booking = {
            'table': table,
            'date': booking_date,
            'time': booking_time,
            'name': name,
            'email': email,
            'phone': phone,        
        }
        return render(request, 'booking/booking_confirmation.html', {'booking': booking})
    else:
        url = reverse('booking_form', args=[table_id, booking_date, booking_time])
        return redirect(url)
