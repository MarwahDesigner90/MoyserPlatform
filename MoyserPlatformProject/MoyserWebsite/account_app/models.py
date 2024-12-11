from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CITIES_IN_SAUDI = [
    ("Riyadh", "Riyadh"),
    ("Jeddah", "Jeddah"),
    ("Makkah", "Makkah"),
    ("Madinah", "Madinah"),
    ("Dammam", "Dammam"),
    ("Khobar", "Khobar"),
    ("Dhahran", "Dhahran"),
    ("Taif", "Taif"),
    ("Tabuk", "Tabuk"),
    ("Abha", "Abha"),
    ("Khamis Mushait", "Khamis Mushait"),
    ("Hail", "Hail"),
    ("Jazan", "Jazan"),
    ("Najran", "Najran"),
    ("Al Baha", "Al Baha"),
    ("Qatif", "Qatif"),
    ("Al Jubail", "Al Jubail"),
    ("Yanbu", "Yanbu"),
    ("Hofuf", "Hofuf"),
    ("Al Ahsa", "Al Ahsa"),
    ("Al Qassim", "Al Qassim"),
    ("Buraidah", "Buraidah"),
    ("Unaizah", "Unaizah"),
    ("Arar", "Arar"),
    ("Sakaka", "Sakaka"),
    ("Al Khafji", "Al Khafji"),
    ("Al Kharj", "Al Kharj"),
    ("Ras Tanura", "Ras Tanura"),
    ("Rabigh", "Rabigh"),
    ("Turaif", "Turaif"),
    ("Al Wajh", "Al Wajh"),
    ("Duba", "Duba"),
    ("Sharurah", "Sharurah"),
    ("Afif", "Afif"),
    ("Al Duwadimi", "Al Duwadimi"),
    ("Al Qaisumah", "Al Qaisumah"),
    ("Al Namas", "Al Namas"),
    ("Baljurashi", "Baljurashi"),
    ("Bisha", "Bisha"),
    ("Mahayel", "Mahayel"),
    ("Wadi ad-Dawasir", "Wadi ad-Dawasir"),
    ("Khafji", "Khafji"),
    ("Samta", "Samta"),
    ("Mecca Region", "Mecca Region"),
    ("Hafar Al-Batin", "Hafar Al-Batin"),
    ("Al Lith", "Al Lith"),
    ("Al Qurayyat", "Al Qurayyat"),
    ("Ad Diriyah", "Ad Diriyah"),
    ("Al Majmaah", "Al Majmaah"),
    ("Hotat Bani Tamim", "Hotat Bani Tamim"),
    ("Al Ola", "Al Ola"),
    ("Sarat Abidah", "Sarat Abidah"),
    ("Dumat Al-Jandal", "Dumat Al-Jandal"),
    ("Al Hawiyah", "Al Hawiyah"),
    ("Thuwal", "Thuwal"),
    ("Muzahmiyah", "Muzahmiyah"),
]

class CompanionUser(models.Model):
    bio = models.TextField()
    bank_account = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    companion = models.OneToOneField(User, on_delete=models.CASCADE, related_name="companion_user")
    hour_rent = models.FloatField()
    skills = models.ManyToManyField("Skill", related_name="companions")
    city = models.CharField(max_length=100, choices=CITIES_IN_SAUDI)
    certification = models.FileField(upload_to="certifications/")
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=[("M", "Male"), ("F", "Female")], default="F")
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.city}"
    
    
    class Skill(models.Model):
        name = models.CharField(max_length=100)

    def __str__(self):
        return self.name