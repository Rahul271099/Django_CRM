from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class doctor_details(models.Model):
    dname = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    dnumber = models.CharField(max_length=10)
    dlocation = models.CharField(max_length=20)
    enter_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    class Meta:
        db_table = 'doctor details'
    
    def __str__(self):
        return str(self.dname)
