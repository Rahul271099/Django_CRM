from django import forms
from .models import doctor_details

class DoctorForm(forms.ModelForm):
    class Meta:
        model = doctor_details
        fields = ['dname', 'specialization', 'dnumber', 'dlocation']
    