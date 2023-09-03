from django.contrib import admin
from .models import Table
from .models import Booking
# from .forms import BookingAdminForm, BookingAdmin
from .forms import BookingAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'table', 'date', 'time')
    list_filter = ('name', 'table', 'date', 'time')
    search_fields = ('name', 'table', 'date', 'time', 'email')   


admin.site.register(Table)
