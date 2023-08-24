from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Booking, Table
from .forms import check_availability_form, BookingForm


def check_available(request):
    form = check_availability_form()
    return render(request, 'booking/check_available.html', {'form': form})

    
def show_available(request):
        
    booking_date = request.GET.get('date')  # Use the variable name 'date'
    booking_time = request.GET.get('time')  # Use the variable name 'time'    

    available_tables = []

    if booking_date and booking_time:
        booked_table_numbers = Booking.objects.filter(date=booking_date, time=booking_time).values_list('table_id', flat=True)
        available_tables = Table.objects.exclude(id__in=booked_table_numbers)
    return render(request, 'booking/show_available.html', {'form': form})    


def create_booking(request, table_id, booking_date, booking_time):
    # Retrieve the table instance based on the table_id
    table = Table.objects.get(id=table_id)

    # Create a new Booking instance
    booking = Booking.objects.create(
        table=table,
        date=booking_date,
        time=booking_time,
        user=request.user  
    )
    return redirect('booking_confirmation', 
                    table_id=table.id, booking_date=booking_date, booking_time=booking_time)    
        

def booking_confirmation(request, table_id, booking_date, booking_time):
    table = Table.objects.get(id=table_id)
    booking = {
        'table': table,
        'date': booking_date,
        'time': booking_time,
        # Add other booking information here
    }
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})        
        

#     initial_data = {'time': booking_time, 'date': booking_date}
    
#     booking_table = request.POST.get('table')  # Extract selected table name
#     if booking_table:
#         initial_data['table'] = booking_table
        
#     if request.user.is_authenticated:
#         user = request.user
#         if user.username:
#             initial_data['name'] = user.username
#         if user.email:
#             initial_data['email'] = user.email        
    
#     booking_form = BookingForm(request.POST or None, initial=initial_data)

#     if request.method == 'POST':
        
#         print("Form submitted")
        
#         if booking_form.is_valid():
        
#             print("Form is valid")
        
#             booking = booking_form.save(commit=False)
#             booking.user = request.user            
            
#             try:
#                 booking.save()
#             except Exception as e:
#                 print("Error while saving booking:", e)            
                
#             return redirect('booking_confirmation', booking_id=booking.id)
        
#         else:
#             print("Form is NOT valid:", booking_form.errors)
#             print("Form data:", request.POST)

#     return render(request, 'booking/show_available.html', {
#         'available_tables': available_tables,
#         'booking_form': booking_form,
#         'booking_date': booking_date, 
#         'booking_time': booking_time, 
#     })

    
# def booking_confirmation(request):
#     booking = get_object_or_404(Booking)
#     return render(request, 'booking_confirmation.html', {'booking': booking})