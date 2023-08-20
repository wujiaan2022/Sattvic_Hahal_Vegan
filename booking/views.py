from django.shortcuts import render
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
        
        booking_form = BookingForm(initial={'time': booking_time, 'date': booking_date})
    
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)  # Bind the form with POST data
            
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