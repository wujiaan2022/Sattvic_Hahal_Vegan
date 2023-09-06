from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from .models import Booking, Table
from .forms import check_availability_form, BookingForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
  

def add_booking(request, table_id, booking_date, booking_time):
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
                
                try:
                    booking.save()
                    print('Booking successful.')                    
                except Exception as e:
                    print("Error while saving booking:", e)
                
                messages.success(request, 'Booking successful! Your table is reserved.')
       
                return redirect('view_booking')
            else:
                print("Form is NOT valid:", form.errors.as_data()) 
        else:
            form = BookingForm(initial=initial_data)   
    
    else:
        if request.method == 'POST':
            form = BookingForm(request.POST, user=None)
            if form.is_valid():
                booking = form.save(commit=False)                
                
                try:
                    booking.save()
                    print('Booking successful.')
                except Exception as e:
                    print("Error while saving booking:", e)
                
                messages.success(request, 'Booking successful! Your table is reserved.')
               
                print("Redirecting to confirm_booking...")
                
                # return redirect('confirm_booking', table_id=table.id, booking_date=booking_date, booking_time=booking_time)
                return redirect('confirm_booking', booking_id=booking.id)

            else:
                print("Form is NOT valid:", form.errors.as_data())   
        else:
            form = BookingForm(initial=initial_data) 

    return render(request, 'booking/add_booking.html', {'form': form, 'table': table, 'booking_date': booking_date, 'booking_time': booking_time})


@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/view_booking.html', context)


def confirm_booking(request, booking_id=None):
    """
    Function enables unlogged guests to view a booking confirmation using the booking ID.
    """
    if booking_id:
        booking = get_object_or_404(Booking, id=booking_id)
        print("Retrieved booking:", booking)
        context = {'booking': booking}
        return render(request, 'booking/confirm_booking.html', context)
    
    return render(request, 'booking/confirm_booking.html')  # Render a template without booking details


@login_required
def edit_booking(request, booking_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/delete_booking.html', context)


def handler404(request, *args, **argv):
    """
    Function to enable customizing 404 error
    page in production environment if booking is not found.
    """
    form = BookingForm()
    context = {
        'form': form
        }
    response = render(request, 'booking/not_found.html', context)
    response.status_code = 404
    return response

