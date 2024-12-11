from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("CANCELLED", "Cancelled"),
]

class Booking(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings_as_companion")
    booking_date_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    
    
    def __str__(self):
        return f"Booking by {self.user.username} on {self.booking_date_time}"