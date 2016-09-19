# coding=utf-8
from django import forms
from models import shareinformation,Linker
from django.forms import ModelForm, Textarea
#from captcha.fields import CaptchaField


# class CaptchaForm(forms.Form):
# checknumber = CaptchaField()





# 用于政资分享模块的表单--xy
class ShareForm(forms.ModelForm):
    class Meta:
        model = shareinformation
        fields = ('projectname', 'projectdirect', 'projectneed', 'projectprocess', 'projectmanage', 'projectlink',
                  'projectsecret',)
        widgets = {'projectprocess': Textarea(attrs={'cols': 40, 'rows': 20}),}


# 用于政资分享模块的表单--xy
class LinkerForm(forms.ModelForm):
    class Meta:
        model = Linker
        fields = ('linkname', 'linkemail', 'linkadress', 'linktelphon', 'remarks', 'secret',)