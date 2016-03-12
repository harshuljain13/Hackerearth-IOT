__author__ = 'h_hack'
from django import forms
from django.contrib.auth.models import User
from .models import Userprofile

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class Userprofileform(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=('watcherid','name','age','sg','bp')


