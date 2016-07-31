#-*- coding:utf-8 -*-

from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from pages import Page
from forms import FRequireInfoForm
from error import Error
import random
import top.api
import pdb


#for SMS verification
appkey='23297047'
secret='45af9457a7d64b7ff5d04162f01d804a'


# Create your views here.

def _do_exception(func):
    def wrapper(request):
        try:
            return func(request)
        except Exception:
            return render(request,Page.require_error,{})

    return wrapper

#@_do_exception
def frame(request):
	form = FRequireInfoForm()
        return render(request,Page.frame,{'form':form})


def verification(request):
    if request.method=='POST':
        mobile_num = request.POST['mobile_num']
        vcode=_send_vcode(mobile_num)
        if vcode!='': #send verification
            #save this number at session
            request.session['vcode'] = str(vcode)
            request.session['mobile_num'] = mobile_num
            return HttpResponse('success')
    
    return HttpResponse('fail')


#@_do_exception
def require_finish(request):
    if request.method == 'POST':
        form = FRequireInfoForm(request.POST)
        err_msg = Error()
        if form.is_valid() and _check_vcode(request) and _check_mobile_num(request):
            del request.session['mobile_num']
            del request.session['vcode']
            form.save()
            #return HttpResponse('success to add this record.')
            return HttpResponseRedirect('/index/')
        elif not _check_vcode(request):
            err_msg.vcode = '无效验证码'
        elif not  _check_mobile_num(request):
            err_msg.mobile_num ='无效手机号码' 
        else:
            err_msg.other = '我们遭遇了一个未预料的错误，请联系管理员'

    else:
        form = FRequireInfoForm()

    return render(request,Page.frame,{'err_msg':err_msg,'form':form})


"""the following part is inner function"""
def _send_vcode(mobile_num):
    """send verification to mobile number.
    Args:
        mobile_num: mobile number.
    return:
        success: vcode string.
        fail: null string.
    """

    vcode=random.randint(1000, 9999)
    req=top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey,secret))

    req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="身份验证"
    req.sms_param='{"code":"%d","product":"雅峙"}'%(vcode)
    req.rec_num=mobile_num
    req.sms_template_code="SMS_4465526"

    try:
	    resp= req.getResponse()
	    return vcode
    except Exception,e:
	    print(e)
	    return ''


def _check_require_type(require_type):
    return True


def _check_vcode(request):
    vcode_s = request.session.get('vcode','invalid')
    vcode_p = request.POST.get('vcode','')
    if vcode_s!='invalid' and vcode_s==vcode_p:
        return True

    return False


def _check_mobile_num(request):
    mobile_num = request.session.get('mobile_num','invalid')
    if mobile_num!='invalid':
        return True

    return False





