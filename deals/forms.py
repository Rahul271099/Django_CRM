from django import forms
from .models import deals

class DealsForm(forms.ModelForm):
    class Meta:
        model = deals
        fields = ['doctor_name','Product_name','quantity']

    
