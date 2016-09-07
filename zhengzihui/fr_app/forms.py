#-*- coding:utf-8 -*-

from django.forms import ModelForm,TextInput
from .models import FRequireInfo

class FRequireInfoForm(ModelForm):
    class Meta:
        model = FRequireInfo
        fields = '__all__'
        widgets = {
            'mobile_num': TextInput(attrs={'placeholder':'手机号码'}),
        }
