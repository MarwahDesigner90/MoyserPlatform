from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("CANCELLED", "Cancelled"),
]

class Booking(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    companion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings_as_companion")
    booking_date_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    
    
    def __str__(self):
        return f"Booking by {self.user.username} on {self.booking_date_time}"
    
class Payment(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - Status: {self.status}"
