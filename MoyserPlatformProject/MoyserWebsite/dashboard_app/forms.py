
from django import forms
from account_app.models import Companion


class CompanionForm(forms.ModelForm):
    class Meta:
        model = Companion
        fields = [
            'bank_account',
            'availability',
            'hour_rent',
            'skills',
            'city',
            'certification',
            'phone_number',
            'gender',
            'age'
        ]
    
    
