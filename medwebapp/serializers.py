__author__ = 'h_hack'

from rest_framework import serializers
from .models import watchervalues,watcherwave


class watcherwaveserializer(serializers.ModelSerializer):
    class Meta:
        model = watcherwave
        fields = ('id', 'watcherid','ppg_pattern','ECG_pattern')


class watcherserializer(serializers.ModelSerializer):
    class Meta:
        model = watchervalues
        fields = ('id', 'watcherid','heart_rate','resp_rate','blood_pressure_sys','blood_pressure_dia','sugar_level',
                  'spo2_content','haemoglobin')