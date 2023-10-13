from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2','date_joined','is_active']

    username = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'})
        )

    first_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'})
        )

    
    last_name = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'})
        )

    email = forms.EmailField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'})
        )
    password1 = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Password','type':'password'})
        )

    password2 = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password','type':'password'})
        )
    
    date_joined = forms.CharField(
            max_length=100,
            required=True,
            widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Confirm Password','type':'date'})
        )
    is_active = forms.BooleanField(required=True)

class UpdateEmployeeForm(UserChangeForm):
    
    is_active = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['first_name','is_active']
    first_name = forms.CharField(
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','readonly':'readonly'})
        )
