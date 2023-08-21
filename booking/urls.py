from django.urls import path
from . import views 

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('show/', views.show_available, name='show_available'),
    
    path('confirmation/<booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]

