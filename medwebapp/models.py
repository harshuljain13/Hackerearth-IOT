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

class relation(models.Model):
    initid = models.CharField(max_length=10)
    relatedid = models.CharField(max_length=10)

    