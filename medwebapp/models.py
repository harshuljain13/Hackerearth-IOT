from __future__ import unicode_literals

from django.db import models

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

    