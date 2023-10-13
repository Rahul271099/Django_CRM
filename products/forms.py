from django import forms
from .models import products
from django.contrib import messages

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['product_name','product_company_name','product_image','product_price']
 
