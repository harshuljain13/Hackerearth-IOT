from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class klopvalues(models.Model):
    klopid = models.CharField(max_length=10)
    heart_rate = models.IntegerField(default=0)
    resp_rate = models.IntegerField(default=0)
    blood_pressure_sys = models.IntegerField(default=0)
    blood_pressure_dia = models.IntegerField(default=0)
    sugar_level = models.IntegerField(default=0)
    spo2_content = models.IntegerField(default=0)
    ECG_pattern = models.CharField(max_length=4000)

class profiles(models.Model):
    klopid = models.CharField(max_length =10,primary_key=True)
    password=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    age = models.IntegerField(default=22)
    sg = models.CharField(max_length=3)
    bp = models.CharField(max_length=3)

class Userprofile(models.Model):
    user = models.OneToOneField(User)
    klopid = models.CharField(max_length =10, primary_key=True)
    name=models.CharField(max_length=20)
    age = models.IntegerField(default=22)
    sg = models.CharField(max_length=3)
    bp = models.CharField(max_length=3)
    def __unicode__(self):
        return self.user.username
