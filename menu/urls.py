from django.urls import path
from . import views 

urlpatterns = [
    path('', views.menu, name='menu'),
    path('dumplings/', views.dumplings, name='dumplings'),
    path('setMenu/', views.setMenu, name='setMenu'),
    
]

