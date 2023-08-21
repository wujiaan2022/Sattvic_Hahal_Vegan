from django.shortcuts import render, get_object_or_404
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
                
                # Create a Booking instance or perform any other actions
                
                # Redirect to a success page or return a response
                return redirect('success_page')  # Replace with the appropriate URL
                
            # If form is not valid, re-render the template with errors
            # The form instance with errors will be used in the template rendering
            
        return render(request, 'booking/show_available.html', {
            'available_tables': available_tables,
            'booking_form': booking_form,
        })
    
    else:
        return render(request, 'booking/show_available.html', {'available_tables': []})
    
    
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})