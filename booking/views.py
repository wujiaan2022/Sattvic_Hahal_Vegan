from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Booking, Table
from .forms import check_availability_form, BookingForm


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})

    
def show_available(request):
    booking_date = request.GET.get('date')
    booking_time = request.GET.get('time')

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

        booking_form = BookingForm(initial=initial_data)

        if request.method == 'POST':
            booking_form = BookingForm(request.POST)        
            
            if booking_form.is_valid():
                # Process the form data
                name = booking_form.cleaned_data['name']
                email = booking_form.cleaned_data['email']
                phone = booking_form.cleaned_data['phone']
                selected_table = booking_form.cleaned_data['table']
                booking_date = booking_form.cleaned_data['date']
                booking_time = booking_form.cleaned_data['time']
                
                booking = booking_form.save()
                booking.user = request.user
                booking.save()
                # messages.success(request, 'Booking successful.')
                return redirect('booking_confirmation', booking_id=booking.id)
            # else:
            #     messages.error(request, 'Booking date must be in the future.')
        return render(request, 'booking/show_available.html', {
            'available_tables': available_tables,
            'booking_form': booking_form,
            'booking': None,
        })
    
    else:
        return render(request, 'booking/show_available.html', {'available_tables': []})             

    
def booking_confirmation(request):
    booking = get_object_or_404(Booking)
    return render(request, 'booking_confirmation.html', {'booking': booking})