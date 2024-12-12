from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('D', 'Completed'),
        ('C', 'Cancelled'),
        
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    companion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companions')
    booking_date_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.companion.username} on {self.booking_date_time}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
       
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)  # Automatically set to now when the payment is created
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Payment for Booking {self.booking.id}: {self.amount} - {self.get_status_display()}"