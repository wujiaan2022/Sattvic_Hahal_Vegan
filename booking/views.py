from django.shortcuts import render
from .forms import BookingForm

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            party_size = form.cleaned_data['party_size']

            # Query available tables
            available_tables = Table.objects.filter(capacity__gte=party_size) \
                                            .exclude(booking__date=date, booking__time=time)

            # Get the selected table ID
            selected_table_id = form.cleaned_data['table']
            selected_table = Table.objects.get(id=selected_table_id)

            # Create a new booking instance and save it
            booking = Booking(table=selected_table, date=date, time=time, party_size=party_size)
            booking.save()

            # Redirect to a success page or display a success message
            return redirect('booking:success')  # Redirect to a success page
    else:
        form = BookingForm()

    context = {'form': form}
    
    return render(request, 'booking/booking_form.html', context)