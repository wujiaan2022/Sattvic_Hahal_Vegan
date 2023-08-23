from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Booking, Table
from .forms import check_availability_form, BookingForm


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

    initial_data = {'time': booking_time, 'date': booking_date}

    if request.user.is_authenticated:
        user = request.user
        if user.username:
            initial_data['name'] = user.username
        if user.email:
            initial_data['email'] = user.email
    
    booking_form = BookingForm(request.POST or None, initial=initial_data)

    if request.method == 'POST':
        
        print("Form submitted")
        
        if booking_form.is_valid():
            
            print("Form is valid")
            
            booking = booking_form.save()
            booking.user = request.user
        
            selected_table_id = request.POST.get('selected_table')
            if selected_table_id:
                booking.table_id = selected_table_id
            
            try:
                booking.save()
            except Exception as e:
                print("Error while saving booking:", e)            
            
            return redirect('booking_confirmation', booking_id=booking.id)
        
        else:
            print("Form is NOT valid:", booking_form.errors)

    return render(request, 'booking/show_available.html', {
        'available_tables': available_tables,
        'booking_form': booking_form,
        'booking_date': booking_date, 
        'booking_time': booking_time, 
    })

    
def booking_confirmation(request):
    booking = get_object_or_404(Booking)
    return render(request, 'booking_confirmation.html', {'booking': booking})