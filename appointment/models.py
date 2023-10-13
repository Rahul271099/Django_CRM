from django.db import models
from django.contrib.auth.models import User
from doctor.models import doctor_details
from django.utils import timezone

# Create your models here.
class appointment(models.Model):
    doct_name = models.ForeignKey(doctor_details,on_delete=models.CASCADE)
    schedule_date = models.DateField(default=timezone.now)
    Schedule_time = models.TimeField(default=timezone.now)
    enterd_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True)

