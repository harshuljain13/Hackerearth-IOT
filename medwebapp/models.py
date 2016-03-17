from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class watcherwave(models.Model):
    watcherid=models.CharField(max_length=10)
    ppg_pattern = models.CharField(max_length=40000,blank=True)
    ECG_pattern = models.CharField(max_length=40000,blank=True)

class watchervalues(models.Model):
    watcherid = models.CharField(max_length=10)
    heart_rate = models.IntegerField(default=0)
    resp_rate = models.IntegerField(default=0)
    blood_pressure_sys = models.IntegerField(default=0)
    blood_pressure_dia = models.IntegerField(default=0)
    sugar_level = models.IntegerField(default=0)
    spo2_content = models.IntegerField(default=0)

class Userprofile(models.Model):
    user = models.OneToOneField(User)
    image_url = models.CharField(max_length=1000, blank=True)
    watcherid = models.CharField(max_length =10, primary_key=True)
    name=models.CharField(max_length=20)
    age = models.IntegerField(default=22)
    sg = models.CharField(max_length=3)
    bp = models.CharField(max_length=3)
    def __unicode__(self):
        return self.user.username


class watcheradvicelist(models.Model):
    watcherid = models.CharField(max_length=10)
    watcheradvice = models.CharField(max_length=2000,blank=True)