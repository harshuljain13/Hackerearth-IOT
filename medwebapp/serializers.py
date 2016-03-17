__author__ = 'h_hack'

from rest_framework import serializers
from .models import watcherdetails,watcherwave


class watcherwaveserializer(serializers.ModelSerializer):
    class Meta:
        model = watcherwave
        fields = ('id', 'watcherid','ppg_pattern','ECG_pattern')


class watcherserializer(serializers.ModelSerializer):
    class Meta:
        model = watcherdetails
        fields = ('watcherid','heart_rate','resp_rate','blood_pressure_sys','blood_pressure_dia','sugar_level',
                  'spo2_content','hb')