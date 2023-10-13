from django.db import models
from django.contrib.auth.models import User
from doctor.models import doctor_details
from products.models import products

# Create your models here.
class deals(models.Model):
    deal_id = models.CharField(max_length=300,blank=True)
    doctor_name = models.ForeignKey(doctor_details,on_delete=models.CASCADE)
    Product_name = models.ForeignKey(products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    entered_by =  models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    