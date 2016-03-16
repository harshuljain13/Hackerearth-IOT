# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-16 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medwebapp', '0005_auto_20160316_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchervalues',
            name='ECG_pattern',
            field=models.CharField(blank=True, max_length=40000),
        ),
        migrations.AlterField(
            model_name='watcherwave',
            name='ECG_pattern',
            field=models.CharField(blank=True, max_length=40000),
        ),
        migrations.AlterField(
            model_name='watcherwave',
            name='ppg_pattern',
            field=models.CharField(blank=True, max_length=40000),
        ),
    ]