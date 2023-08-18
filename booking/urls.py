from django.urls import path
from . import views

urlpatterns = [
    # path('', views.book_table, name='book_table'),
    path('', views.check_availability, name='check-availability'),
]