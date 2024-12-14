from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL

STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("COMPLETED", "Completed"),
]

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference user model
    companion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings_as_companion")
    booking_date_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    
    def __str__(self):
        return f"Booking by {self.user.username} on {self.booking_date_time}"

