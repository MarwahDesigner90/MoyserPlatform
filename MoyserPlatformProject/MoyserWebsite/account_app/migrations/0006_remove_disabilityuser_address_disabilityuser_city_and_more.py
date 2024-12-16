# Generated by Django 5.1.4 on 2024-12-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0005_alter_companion_image_alter_disabilityuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disabilityuser',
            name='address',
        ),
        migrations.AddField(
            model_name='disabilityuser',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh'), ('Al-kharj', 'Al-kharj'), ('Al-majmaah', 'Al-majmaah'), ('Afif', 'Afif'), ('Jeddah', 'Jeddah'), ('Makkah', 'Makkah'), ('Al-Taif', 'Al-Taif'), ('Rabigh', 'Rabigh'), ('Al-Madinah', 'Al-Madinah'), ('Dammam', 'Dammam'), ('Al-Ahsa', 'Al-Ahsa'), ('Jizan', 'Jizan'), ('Najran', 'Najran'), ('Al-jawf', 'Al-jawf'), ('Abha', 'Abha'), ('Bisha', 'Bisha'), ('Tabuk', 'Tabuk'), ('Hail', 'Hail'), ('Qassim', 'Qassim')], default='Riyadh', max_length=50),
        ),
        migrations.AlterField(
            model_name='companion',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh'), ('Al-kharj', 'Al-kharj'), ('Al-majmaah', 'Al-majmaah'), ('Afif', 'Afif'), ('Jeddah', 'Jeddah'), ('Makkah', 'Makkah'), ('Al-Taif', 'Al-Taif'), ('Rabigh', 'Rabigh'), ('Al-Madinah', 'Al-Madinah'), ('Dammam', 'Dammam'), ('Al-Ahsa', 'Al-Ahsa'), ('Jizan', 'Jizan'), ('Najran', 'Najran'), ('Al-jawf', 'Al-jawf'), ('Abha', 'Abha'), ('Bisha', 'Bisha'), ('Tabuk', 'Tabuk'), ('Hail', 'Hail'), ('Qassim', 'Qassim')], max_length=50),
        ),
        migrations.AlterField(
            model_name='disabilityuser',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='disabilityuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('orientation_and_mobility', 'Orientation and Mobility'), ('Reading_instructions', 'Reading the instructions'), ('assistive_technology', 'Assistive Technology'), ('sign_language_interpretation', 'Sign Language Interpretation'), ('lip_reading', 'Lip Reading'), ('auditory_training', 'Auditory Training'), ('mobility_assistance', 'Mobility Assistance'), ('physical_therapy', 'Physical Therapy'), ('wheelchair_management', 'Wheelchair Management'), ('life_skills_coaching', 'Life Skills Coaching'), ('personal_care_assistance', 'Personal Care Assistance'), ('communication_aids', 'Communication Aids')], max_length=100, unique=True),
        ),
    ]
