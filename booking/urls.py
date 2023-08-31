from django.urls import path
from . import views 

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('show/', views.show_available, name='show_available'),
    path('add/<int:table_id>/<str:booking_date>/<str:booking_time>/', views.add_booking, name='add_booking'),
    path('view/', views.view_booking, name='view_booking'),
    path('confirm/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]

