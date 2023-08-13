from django.db import models


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
    name = models.CharField(max_length=100)  
    email = models.EmailField()             
    phone = models.CharField(max_length=20)  
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()     

    def __str__(self):
        return f"Booking for {self.party_size} people on {self.date} at {self.time}"