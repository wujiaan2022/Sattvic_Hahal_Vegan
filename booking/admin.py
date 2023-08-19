from django.contrib import admin
from .models import Table
from .models import Booking
from .forms import BookingAdminForm


class BookingAdmin(admin.ModelAdmin):
    form = BookingAdminForm


admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)