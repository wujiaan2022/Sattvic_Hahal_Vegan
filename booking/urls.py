from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.check_available, name='check_available'),
    path('show', views.show_available, name='show_available'),
]