# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medwebapp', '0002_auto_20160305_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]