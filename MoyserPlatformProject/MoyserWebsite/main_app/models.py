from django.db import models
from account_app.models import DisabilityUser
# Create your models here.

class Feedback(models.Model):
    RATING_CHOICES = [
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ]

    disability_user = models.OneToOneField(DisabilityUser, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self):
        return f"Feedback from {self.disability_user.user.username}: {self.rating} Stars"