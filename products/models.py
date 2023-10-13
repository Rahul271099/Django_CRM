from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=200)
    product_company_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="media",default=None)
    product_price = models.FloatField(default=0.00)
    enterd_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return f'{self.product_name}'