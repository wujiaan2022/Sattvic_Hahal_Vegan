from django.contrib.auth.models import User
from django.db import models
import uuid


class Table(models.Model):
    CAPACITY_CHOICES = (
        (2, '2 people (Privacy and Garden View)'),
        (4, '4 people'),
        (8, '8 people (Round Table with Rotating Tray)'),
    )

    capacity = models.IntegerField(choices=CAPACITY_CHOICES)

    table_name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Table {self.table_name} - {self.get_capacity_display()}"


class Booking(models.Model):
    
    TIME_CHOICES = [
    ('12:00 for Lunch', '12:00 Lunch Time'),
    ('18:00 for Dinner', '18:00 Dinner Time'),]
    
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             default=None,
                             on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)  
    email = models.EmailField()             
    phone = models.CharField(max_length=20, null=True, blank=True)  
    party_size = models.IntegerField(null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=20, choices=TIME_CHOICES)     

    def __str__(self):
        return f"Booking for {self.party_size} people on {self.date} at {self.time}"