import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Database schemas intilization
class City (models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    district = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.city_id)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    blood_bank_name = models.CharField(max_length=120, blank=False)
    username = models.CharField(max_length=40, unique=True, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=10, default="N/A", blank=False)
    address = models.CharField(max_length=400, default="N/A", blank=False)
    roles = models.CharField(max_length=20, default="N/A", blank=False) #blood_bank : for role based restriction
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user_id)

class RBC(models.Model):
    rbc_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #blood_details = models.ForeignKey(Blood_details, on_delete=models.CASCADE)
    # type_name =  models.CharField(max_length=120, blank=False) #platelets, WBC, RBC, other types then each each their own class.
    quantity_ABpstv = models.IntegerField(default=0, blank=False)
    quantity_ABngtv = models.IntegerField(default=0, blank=False)
    quantity_Apstv = models.IntegerField(default=0, blank=False)
    quantity_Angtv = models.IntegerField(default=0, blank=False)
    quantity_Bpstv = models.IntegerField(default=0, blank=False)
    quantity_Bngtv = models.IntegerField(default=0, blank=False)
    quantity_Opstv = models.IntegerField(default=0, blank=False)
    quantity_Ongtv = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.rbc_id)

class Platelets(models.Model):
    platelets_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_ABpstv = models.IntegerField(default=0, blank=False)
    quantity_ABngtv = models.IntegerField(default=0, blank=False)
    quantity_Apstv = models.IntegerField(default=0, blank=False)
    quantity_Angtv = models.IntegerField(default=0, blank=False)
    quantity_Bpstv = models.IntegerField(default=0, blank=False)
    quantity_Bngtv = models.IntegerField(default=0, blank=False)
    quantity_Opstv = models.IntegerField(default=0, blank=False)
    quantity_Ongtv = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.platelets_id)

class Plasma(models.Model):
    plasma_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_ABpstv = models.IntegerField(default=0, blank=False)
    quantity_ABngtv = models.IntegerField(default=0, blank=False)
    quantity_Apstv = models.IntegerField(default=0, blank=False)
    quantity_Angtv = models.IntegerField(default=0, blank=False)
    quantity_Bpstv = models.IntegerField(default=0, blank=False)
    quantity_Bngtv = models.IntegerField(default=0, blank=False)
    quantity_Opstv = models.IntegerField(default=0, blank=False)
    quantity_Ongtv = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.plasma_id)

class CryoAHF(models.Model):
    cryo_ahf_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_ABpstv = models.IntegerField(default=0, blank=False)
    quantity_ABngtv = models.IntegerField(default=0, blank=False)
    quantity_Apstv = models.IntegerField(default=0, blank=False)
    quantity_Angtv = models.IntegerField(default=0, blank=False)
    quantity_Bpstv = models.IntegerField(default=0, blank=False)
    quantity_Bngtv = models.IntegerField(default=0, blank=False)
    quantity_Opstv = models.IntegerField(default=0, blank=False)
    quantity_Ongtv = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.cryo_ahf_id)

class Granulocytes(models.Model):
    granulocytes_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_ABpstv = models.IntegerField(default=0, blank=False)
    quantity_ABngtv = models.IntegerField(default=0, blank=False)
    quantity_Apstv = models.IntegerField(default=0, blank=False)
    quantity_Angtv = models.IntegerField(default=0, blank=False)
    quantity_Bpstv = models.IntegerField(default=0, blank=False)
    quantity_Bngtv = models.IntegerField(default=0, blank=False)
    quantity_Opstv = models.IntegerField(default=0, blank=False)
    quantity_Ongtv = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.granulocytes_id)
