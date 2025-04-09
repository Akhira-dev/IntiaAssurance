# forms.py
from django import forms
from .models import Insurance

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['client', 'manager', 'insurance_type', 'expiration_date']
