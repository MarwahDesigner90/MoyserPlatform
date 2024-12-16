# Generated by Django 5.1.4 on 2024-12-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('orientation_and_mobility', 'Orientation and Mobility'), ('Reading_instructions', 'Reading the instructions'), ('assistive_technology', 'Assistive Technology'), ('sign_language_interpretation', 'Sign Language Interpretation'), ('lip_reading', 'Lip Reading'), ('auditory_training', 'Auditory Training'), ('mobility_assistance', 'Mobility Assistance'), ('physical_therapy', 'Physical Therapy'), ('wheelchair_management', 'Wheelchair Management'), ('life_skills_coaching', 'Life Skills Coaching'), ('personal_care_assistance', 'Personal Care Assistance'), ('communication_aids', 'Communication Aids'), ('first_aid', 'First Aid and Emergency Response'), ('cultural_respect', 'Respect for Cultural, Religious, and Personal Preferences'), ('mental_health_awareness', 'Mental Health Awareness'), ('problem_solving', 'Problem-Solving Skills'), ('other', 'Other')], max_length=100, unique=True),
        ),
    ]
