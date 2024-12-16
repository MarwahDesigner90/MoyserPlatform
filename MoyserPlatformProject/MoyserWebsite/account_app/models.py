from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here. 


class User(AbstractUser):
    ROLE_CHOICES = [
        ('companion', 'Companion'),
        ('beneficiary', 'Beneficiary'),
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
        ('other', 'Other'),  # Option for custom skills
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
        ('City1', 'Riyadh'),
        ('City2', ' Al-kharj'),
        ('City3', 'Al-majmaah'),
        ('City4', 'Afif'),
        ('City5', 'Jeddah'),
        ('City6', 'Makkah'),
        ('City7', 'Al-Taif'),
        ('City8', 'Rabigh'),
        ('City9', 'Al-Madinah'),
        ('City10','Dammam'),
        ('City11', 'Al-Ahsa'),
        ('City12', 'Jizan'),
        ('City14', 'Najran'),
        ('City15', 'Al-jawf'),
        ('City16', 'Abha'),
        ('City17', 'Bisha'),
        ('City18', 'Tabuk'),
        ('City19', 'Hail'),
        ('City20', 'Qassim'),
    ]

    companion = models.OneToOneField(User, on_delete=models.CASCADE , related_name= "compinon_user")
    bank_account = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    hour_rent = models.FloatField()
    skills = models.ManyToManyField(Skill)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    certification = models.FileField(upload_to='pdf/', blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

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

    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=15)
    disability_type = models.CharField(max_length=2, choices=DISABILITY_TYPE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username 