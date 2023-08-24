from django.urls import path
from . import views 

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('show/', views.show_available, name='show_available'),
    path('create_booking/<int:table_id>/<str:booking_date>/<str:booking_time>/', 
         view.create_booking, name='create_booking'),
    path('booking_confirmation/<int:table_id>/<str:booking_date>/<str:booking_time>/', 
         views.booking_confirmation, name='booking_confirmation'),
]

