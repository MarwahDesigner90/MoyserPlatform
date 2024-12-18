from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here. 


class User(AbstractUser):
    ROLE_CHOICES = [
        ('companion', 'Companion'),
        ('beneficiary', 'Beneficiary'),
        ('admin', 'Admin'),

    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='beneficiary')
    

    def __str__(self):
        return self.username

class Skill(models.Model):
    SKILL_CHOICES = [
        ('orientation_and_mobility', 'Orientation and Mobility'),
        ('Reading_instructions', 'Reading the instructions'),
        ('assistive_technology', 'Assistive Technology'),
        ('sign_language_interpretation', 'Sign Language Interpretation'),
        ('lip_reading', 'Lip Reading'),
        ('auditory_training', 'Auditory Training'),
        ('mobility_assistance', 'Mobility Assistance'),
        ('physical_therapy', 'Physical Therapy'),
        ('wheelchair_management', 'Wheelchair Management'),
        ('life_skills_coaching', 'Life Skills Coaching'),
        ('personal_care_assistance', 'Personal Care Assistance'),
        ('communication_aids', 'Communication Aids'),
  
    ]

    name = models.CharField(max_length=100, choices=SKILL_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Companion(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CITY_CHOICES = [
    ('Riyadh', 'Riyadh'),
    ('Al-kharj', 'Al-kharj'),
    ('Al-majmaah', 'Al-majmaah'),
    ('Afif', 'Afif'),
    ('Jeddah', 'Jeddah'),
    ('Makkah', 'Makkah'),
    ('Al-Taif', 'Al-Taif'),
    ('Rabigh', 'Rabigh'),
    ('Al-Madinah', 'Al-Madinah'),
    ('Dammam', 'Dammam'),
    ('Al-Ahsa', 'Al-Ahsa'),
    ('Jizan', 'Jizan'),
    ('Najran', 'Najran'),
    ('Al-jawf', 'Al-jawf'),
    ('Abha', 'Abha'),
    ('Bisha', 'Bisha'),
    ('Tabuk', 'Tabuk'),
    ('Hail', 'Hail'),
    ('Qassim', 'Qassim'),
]

    companion = models.OneToOneField(User, on_delete=models.CASCADE , related_name= "compinon_user")
    bank_account = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    hour_rent = models.FloatField()
    skills = models.ManyToManyField(Skill)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    certification = models.FileField(upload_to='pdf/', null=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpeg')

    def __str__(self):
        return f"{self.companion.username} - {self.city}"
    


class DisabilityUser(models.Model):
    DISABILITY_TYPE_CHOICES = [
        ('VI', 'Visually Impaired'),
        ('HI', 'Hearing Impaired'),
        ('MD', 'Mobility Disability'),
        ('OD', 'Other Disability'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CITY_CHOICES = [
        ('Riyadh', 'Riyadh'),
        ('Al-kharj', 'Al-kharj'),
        ('Al-majmaah', 'Al-majmaah'),
        ('Afif', 'Afif'),
        ('Jeddah', 'Jeddah'),
        ('Makkah', 'Makkah'),
        ('Al-Taif', 'Al-Taif'),
        ('Rabigh', 'Rabigh'),
        ('Al-Madinah', 'Al-Madinah'),
        ('Dammam', 'Dammam'),
        ('Al-Ahsa', 'Al-Ahsa'),
        ('Jizan', 'Jizan'),
        ('Najran', 'Najran'),
        ('Al-jawf', 'Al-jawf'),
        ('Abha', 'Abha'),
        ('Bisha', 'Bisha'),
        ('Tabuk', 'Tabuk'),
        ('Hail', 'Hail'),
        ('Qassim', 'Qassim'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15, blank=True) 
    disability_type = models.CharField(max_length=2, choices=DISABILITY_TYPE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(null=True)  
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default='Riyadh')
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpeg')

    def __str__(self):
        return self.user.username