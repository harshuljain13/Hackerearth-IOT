__author__ = 'h_hack'

from rest_framework import serializers
from .models import watchervalues,profiles

class watcherserializer(serializers.ModelSerializer):
    class Meta:
        model = watchervalues
        fields = ('id', 'watcherid','heart_rate','resp_rate','blood_pressure_sys','blood_pressure_dia','sugar_level',
                  'spo2_content','ECG_pattern')

class profserializer(serializers.ModelSerializer):
    class Meta:
        model = profiles
        fields = ('id', 'watcherid','password','name','age','sg','bp')