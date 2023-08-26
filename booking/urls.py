from django.urls import path
from . import views 

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('show/', views.show_available, name='show_available'),
    path('booking/<int:table_id>/<str:booking_date>/<str:booking_time>/', views.booking_form, name='booking_form'),
    path('confirmation/<int:table_id>/<str:booking_date>/<str:booking_time>/', views.booking_confirmation, name='booking_confirmation'),
]

