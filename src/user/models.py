import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Database schemas intilization

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    blood_bank_name = models.CharField(max_length=120, blank=False)
    username = models.CharField(max_length=40, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=10, default="N/A", blank=False)
    address = models.CharField(max_length=400, default="N/A", blank=False)
    
    def __str__(self):
        return str(self.user_id)

class Blood_info(models.Model):
    bloodtype_id = models.AutoField(primary_key=True)
    type_name =  models.CharField(max_length=120, blank=False) #platelets, WBC, RBC, other types then each each their own class.
    