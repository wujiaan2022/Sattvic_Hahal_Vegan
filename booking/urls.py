from django.urls import path
from . import views 

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('show/', views.show_available, name='show_available'),
    path('add/<int:table_id>/<str:booking_date>/<str:booking_time>/', views.add_booking, name='add_booking'),
    path('view/', views.view_booking, name='view_booking'),
    
    path('confirmation/<int:table_id>/<str:booking_date>/<str:booking_time>/', views.booking_confirmation, name='booking_confirmation'),
]

