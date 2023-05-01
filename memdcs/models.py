from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length = 50)
    father_name = models.CharField(max_length = 50)
    ward_num = models.IntegerField()
    contact_num = models.IntegerField()
    cows = models.IntegerField()
    buffaloes = models.IntegerField()
    total_milk_produced = models.IntegerField()
    balance_milk_remaining = models.IntegerField()
    selling_to_sudha = models.BooleanField()
    selling_to_other_whom = models.CharField(max_length = 50)
    selling_to_other_rate = models.CharField(max_length = 50)
    village_code = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().pk)

class AdditionalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobilenum = models.IntegerField()
    union = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

class VillageData(models.Model):
    village_code = models.IntegerField()
    village_name = models.CharField(max_length=50)
    panchayat_code = models.IntegerField()
    panchayat_name = models.CharField(max_length=50)
    block_code = models.IntegerField()
    block_name = models.CharField(max_length=50)
    district_code = models.IntegerField()
    district_name = models.CharField(max_length=50)
    state_code = models.IntegerField()
    state_name = models.CharField(max_length=50)