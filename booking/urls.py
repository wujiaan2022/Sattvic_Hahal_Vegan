from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.check_availability, name='check_availability'),
]