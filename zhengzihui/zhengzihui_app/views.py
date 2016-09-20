
#coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse as HR
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from itertools import chain
import random

import random
import top.api
import sys
import datetime
import time
import json #用来将字典类型的数据序列化，然后传给模板以及js,不能序列化model实例
import jieba,p_alipay.alipay
from token import Token
from django.core.mail import send_mail
from django.core import serializers #用来序列化model 传给js
#from models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item,tb_item_pa,tb_item_class,tb_goods,tb_album,tb_pic,tb_article,tb_goods_evaluation,tb_goods_click,tb_goods_class,tb_order,tb_item_click,tb_area
from models import *
from yz_views import *
from xcz_views import *
#by-xy
from forms import ShareForm,LinkerForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from models import Linker

SECRET_KEY = '+a^0qwojpxsam*xa5*y_5o+#9fej#+w72m998sjc!e)oj9im*y'
token_confirm = Token(SECRET_KEY)
appkey='23297047'
secret='45af9457a7d64b7ff5d04162f01d804a'

reload(sys)
sys.setdefaultencoding('utf8')
# Create your views here.

#zss条件筛选
def filter_labels(request):
    keys = request.GET['filterkeys']
    if 'bumen' in request.GET:
        request.session['bumen'] = keys    
    if 'jibie' in request.GET:
        request.session['jibie'] = keys 
    if 'zhuangtai' in request.GET:
        request.session['zhuangtai'] = keys
    return HttpResponseRedirect('/search_result/')


def order_completed(request):
    if request.GET['goodsid']:
        goodsid = request.GET['goodsid']
        return render(request,'order_completed.html',{'goodsid':goodsid,})




def declare(request):
	id1 = request.GET.get('itemid')
	#print id1
	tb_goods_list = tb_goods.objects.filter(item_id=id1)
	#for a in tb_goods_list: 
			#print (a.goods_id)
	return render_to_response('goods_list.html',{'tb_goods_list':tb_goods_list})


#zss
#用户中心
def user_center(request):
    #request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    user = []
    a_click_items = []
    #a_recommend_items = []
    if 'user_id' in request.COOKIES:
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")
    if user.user_type == 0:
        click_items = tb_item_click.objects.order_by('-click_counter')[:15]#获取点击率前15的项目
        for click_item in click_items:
            a_click_item = {}
            a_click_item['id'] = click_item.item_id#获取项目id
            a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
            album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_click_items.append(a_click_item)

    else:
        _industry = user.expand.company_industry
        click_items = tb_item.objects.filter(item_about__contains = _industry)
        for click_item in click_items:
            a_click_item = {}
            a_click_item['id'] = click_item.item_id  # 获取项目id
            a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name  # 获取项目名字
            album = tb_album.objects.filter(album_type=0, affiliation_id=click_item.item_id, is_default=1).order_by('-nacl_sort')[0]  # 获取项目对应的相册id
            album_id = album.album_id
            a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_click_items.append(a_click_item)
    '''recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]#获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item= {}
        a_recommend_item['id'] = recommend_item.item_id#获取项目id
        a_recommend_item['name'] = recommend_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=recommend_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)'''
    return render(request,'user.html',{'user':user,'a_click_items':a_click_items})


#总览 cyf
#def view_all(request):
   # return HttpResponse("hello world")




#用户信息 zss

    #我的信息
def my_info(request):
    user = []
    company = []
    usertype = False
    if request.COOKIES['user_id']:
        #print("2222")
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
        if user.user_type == 1:
            company = tb_user_expand.objects.get(user_id=user_id)
            usertype = True
    return render(request,'my_info.html',{'user':user,'company':company,'usertype':usertype})

    #保存修改信息
def modify_user(request):
    user = []
    user_expand = []
    if request.session['user_id']:
        user_id = int(request.session['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    user.user_name = request.POST['name']
    user.user_email = request.POST['email']
    user.user_password = request.POST['password']
    user.user_telephone = request.POST['phonenumber']
    usertype = int(request.POST['usertype'])
    user.user_type = usertype
    user.save()
    if usertype == 1:
        user_expand = tb_user_expand.objects.get(user_id=user.user_id)
        user_expand.company_tel = request.POST['company_tel']
        user_expand.company_email = request.POST['company_email']
        user_expand.company_name = request.POST['company_name']
        user_expand.company_district = request.POST['company_district']
        user_expand.company_address = request.POST['company_address']
        user_expand.company_registered_capital = request.POST['company_registered_capital']
        user_expand.company_industry = request.POST['company_industry']
        user_expand.company_stuff_no = request.POST['company_stuff_no']
        user_expand.company_nature = request.POST['company_nature']
        user_expand.save()
    return HttpResponseRedirect('/zzh/user_center')
    
#lqx
#商家中心
def merchant_center(request):
    #request.session['user_id'] = 3#此处设置了个session值用来测试，等登录模块完成之后再修改
    sp = []
    if 'sp_id' in request.COOKIES:
        sp_id = int(request.COOKIES['sp_id'])
        sp = tb_service_provider.objects.get(sp_id=sp_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")

    return render(request,'shenbaohezuo.html',{'sp':sp,})

    
    #保存登录商家修改信息
def modify_merchant(request):
    sp = []
    sp_expand = []
    if request.COOKIES['sp_id']:
        sp_id = int(request.COOKIES['sp_id'])
        sp = tb_service_provider.objects.get(sp_id=sp_id)
    sp.sp_name = request.POST['name']
    sp.sp_email = request.POST['email']
    sp.sp_password = request.POST['password']
    sp.sp_telephone = request.POST['phonenumber']
    sptype = int(request.POST['sptype'])
    sp.sp_type = request.POST['sp_type']
    

    return HttpResponseRedirect('/zzh/merchant_center')
##商家登录页面        
def merchant(request):
    errors= []  
    sp_name=None  
    password=None
    sp = tb_service_provider()
    if 'sp_id' in request.COOKIES:
        response = render(request,'bus_index.html',{})
        return response
        
    if request.method == 'POST' :  
        if not request.POST.get('_spname'):  
            errors.append('请输入用户名')  
        else:
            sp_name = request.POST.get('_spname')  
        if not request.POST.get('password'):  
            errors.append('请输入登陆密码')  
        else:  
            password= request.POST.get('password')  
        if sp_name is not None and password is not None:
            try:
                sp = tb_service_provider.objects.get(sp_name = sp_name)
            except tb_service_provider.DoesNotExist:
                errors.append('用户名不存在')
            
            	return render_to_response('merchant.html', {'errors': errors})
            if password == sp.psw:
                sp_type1=request.POST.get('sp_type1')
                #ms:print "testing..."
                #print sp_type
                
                if sp_type1=="sp_typetwo":
                  return render(request,"testpage1.html")
                  
                if sp_type1=="sp_typethree":
                  return render(request,"testpage1.html")

                response = HttpResponseRedirect('/busindex/')#render(request,'bus_index.html',{})#HttpResponseRedirect('/busindex/')
                
                response.set_cookie('sp_name',sp_name,3600)
                response.set_cookie('sp_id',sp.sp_id,3600)
                #print(user.expand.company_name)
                return response
            else:
                errors.append('密码错误')
    return render_to_response('merchant.html', {'errors': errors})    
###商家退出
def merchantout(request):
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('sp_name')
        response.delete_cookie('sp_id')
        return response    
    
    #安全中心
def safe_center(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])

    #支付绑定
def pay_combine(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])

    #等级与成长
def grade_grow(request):
    if request.session['user_id']:
        user_id = int(request.session['user_id'])


#订单管理 zss
    #全部订单
def all_orders(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['order_no'] = order.order_no#获取订单编号
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        a_order['add_time'] = order.add_time#获取起始时间
        if order.lock_state == 0:
            if order.order_state == 0:
                a_order['order_state'] = '已取消'
            if order.order_state == 1:
                a_order['order_state'] = '未付款'
            if order.order_state == 2:
                a_order['order_state'] = '已付款'
            if order.order_state == 3:
                a_order['order_state'] = '已发货' 
            if order.order_state == 4:
                a_order['order_state'] = '已验收'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

##qiu
def all_orders_back(request):
    user = []
    a_click_items = []
    a_recommend_items = []
    if 'user_id' in request.COOKIES:
        user_id = int(request.COOKIES['user_id'])
        user = tb_user.objects.get(user_id=user_id)
    else:
        return HttpResponse("请先登录账号;请返回到上级页面登录或者注册")

    click_items = tb_item_click.objects.order_by('-click_counter')[:15]#获取点击率前15的项目
    for click_item in click_items:
        a_click_item = {}    
        a_click_item['id'] = click_item.item_id#获取项目id
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga#获取项目资助金额
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        item=tb_item.objects.get(item_id=click_item.item_id)
        item_pa_id=item.item_pa_id
        a_click_item['ipa_name'] = tb_item_pa.objects.get(ipa_id=item_pa_id).ipa_name#获取项目管理单位名称
        
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_click_item['item_publish'] = tb_item.objects.get(item_id=click_item.item_id).item_publish.strftime('%Y.%m.%d')#获取项目开始时间
        a_click_item['item_deadtime'] = tb_item.objects.get(item_id=click_item.item_id).item_deadtime.strftime('%Y.%m.%d')#获取项目截止时间
        start_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_click_item['item_consume_time'] = 100
            a_click_item['item_key'] = "已结束"
        else:
            a_click_item['item_consume_time'] = int(consume_time)
        a_click_items.append(a_click_item)
    recommend_items = tb_item.objects.filter(is_recommend=1).order_by('-item_id')[:15]#获取推荐的前15的项目
    for recommend_item in recommend_items:
        a_recommend_item= {}
        a_recommend_item['id'] = recommend_item.item_id#获取项目id
        a_recommend_item['name'] = recommend_item.item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=recommend_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_recommend_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_recommend_items.append(a_recommend_item)
    
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['order_no'] = order.order_no#获取订单编号
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        a_order['add_time'] = order.add_time#获取起始时间
        if order.lock_state == 0:
            if order.order_state == 0:
                a_order['order_state'] = '已取消'
            if order.order_state == 1:
                a_order['order_state'] = '未付款'
            if order.order_state == 2:
                a_order['order_state'] = '已付款'
            if order.order_state == 3:
                a_order['order_state'] = '已发货' 
            if order.order_state == 4:
                a_order['order_state'] = '已验收'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_back.html',{'user':user,'a_click_items':a_click_items,'a_recommend_items':a_recommend_items,'a_order_list':a_order_list})
    
    
    
    #未支付
def not_pay(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=3).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id 
        a_order['goods_id'] = order.goods_id#获取商品id     
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '未付款'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

    #已支付
def payed(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=2).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已付款'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #已发货
def delivered(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=3).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id   
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已发货'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #已验收
def checked(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=4).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已验收'
        else:
            a_order['order_state'] = '申请处理中'
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})

    #已取消
def delete(request):
    order_list = []
    a_order_list = []
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_list = tb_order.objects.filter(buyer_id=user_id,order_state=0).order_by('-add_time')

    for order in order_list:
        a_order = {}
        a_order['order_id'] = order.order_id#获取订单id
        a_order['goods_id'] = order.goods_id#获取商品id      
        a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        a_order['item_id'] = order.item_id#获取项目id
        if order.lock_state == 0: 
            a_order['order_state'] = '已取消'
        else:
            a_order['order_state'] = '申请处理中'    
        a_order['order_amount'] = order.order_amount
        if order.eval_state == 0:
            a_order['eval_state'] = '未评价'
        else:
            a_order['eval_state'] = '已评价'
        ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
        a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
        album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_order_list.append(a_order)
    return render(request,'order_list.html',{'a_order_list':a_order_list})


    #确认订单
def order_enter(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.order_state = 4
            order.save()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    #申请关闭
def order_giveup(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.lock_state = 1
            order.save()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

        
    #删除订单
def order_delete(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            order.delete()
            return HttpResponse("0")
        else:
            return HttpResponse("1")

    #去评价
def order_commit(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.GET['id']
        order = tb_order.objects.get(order_id=order_id)
        if order.buyer_id == user_id:
            a_order = {}
            a_order['order_id'] = order.order_id#获取订单id
            a_order['goods_id'] = order.goods_id#获取商品id    
            a_order['item_id'] = order.item_id#获取项目id
            a_order['goods_name'] = tb_goods.objects.get(goods_id=order.goods_id).goods_name#获取商品的名字
        
            a_order['order_amount'] = order.order_amount
            ipa_id = tb_item.objects.get(item_id=order.item_id).item_pa_id
            a_order['publish'] = tb_item_pa.objects.get(ipa_id=ipa_id).ipa_name
            album = tb_album.objects.filter(album_type=0,affiliation_id=order.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_order['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示    
            return render(request,'order_commit.html',{'order':a_order})
    #添加评价
def order_add_commit(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        order_id = request.POST['order_id']
        order = tb_order.objects.get(order_id=order_id)
        goods_id = order.goods_id
        user_name = order.buyer_name
        goods = tb_goods.objects.get(goods_id=goods_id)
        goods_name = goods.goods_name
        if order.buyer_id == user_id:
            if tb_goods_evaluation.objects.all().order_by('-goev_id'):
                goev_id = tb_goods_evaluation.objects.all().order_by('-goev_id')[0].goev_id + 1 #id自增
            else:
                goev_id = 0
            goev_desccredit = int(request.POST['complete'])
            goev_servicecredit = int(request.POST['service'])
            goev_content = request.POST['content']
            is_anonymous = int(request.POST['is_anonymous'])
            tb_goods_evaluation.objects.create(goev_id=goev_id,order_id=order_id,goods_id=goods_id,goods_name=goods_name,user_id=user_id,user_name=user_name,goev_desccredit=goev_desccredit,goev_servicecredit=goev_servicecredit,goev_content=goev_content,is_anonymous=is_anonymous)
            order.eval_state = 1
            order.save()
            return render(request,'commit_complete.html',{})


#评价管理

    #我的评价
def my_evaluate(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        a_evaluations = []
        evaluations = tb_goods_evaluation.objects.filter(user_id=user_id).order_by('-create_time')
        for evaluation in evaluations:
            a_evaluation = {}
            goods_id = evaluation.goods_id
            a_evaluation['goods_id'] = goods_id
            a_evaluation['goods_name'] = evaluation.goods_name
            a_evaluation['create_time'] = evaluation.create_time.strftime('%Y.%m.%d')
            a_evaluation['goev_desccredit'] = evaluation.goev_desccredit
            a_evaluation['goev_servicecredit'] = evaluation.goev_servicecredit
            a_evaluation['goev_content'] = evaluation.goev_content
            
            if evaluation.is_anonymous == 0:
                a_evaluation['is_anonymous'] = '不匿名'
            else:
                a_evaluation['is_anonymous'] = '匿名'
            item_id = tb_goods.objects.get(goods_id=goods_id).item_id
            album = tb_album.objects.filter(album_type=0,affiliation_id=item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
            album_id = album.album_id
            a_evaluation['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            a_evaluations.append(a_evaluation)
            
        return render(request,'my_evaluate.html',{'evaluations':a_evaluations})


    #评价统计
def statistics(request):
    if request.COOKIES['user_id']:
        user_id = int(request.COOKIES['user_id'])
        all_orders = len(tb_order.objects.filter(buyer_id=user_id))
        all_commit = len(tb_goods_evaluation.objects.filter(user_id=user_id))
        not_commit = all_orders - all_commit
        desccredit_1 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=1))
        desccredit_2 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=2))
        desccredit_3 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=3))
        desccredit_4 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=4))
        desccredit_5 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_desccredit=5))

        servicecredit_1 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=1))
        servicecredit_2 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=2))
        servicecredit_3 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=3))
        servicecredit_4 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=4))
        servicecredit_5 = len(tb_goods_evaluation.objects.filter(user_id=user_id,goev_servicecredit=5))
        json.dumps('all_orders',all_orders)
        json.dumps('all_commit',all_commit)
        json.dumps('not_commit',not_commit)
        json.dumps('desccredit_1',desccredit_1)
        json.dumps('desccredit_2',desccredit_2)
        json.dumps('desccredit_3',desccredit_3)
        json.dumps('desccredit_4',desccredit_4)
        json.dumps('desccredit_5',desccredit_5)
        json.dumps('servicecredit_1',servicecredit_1)
        json.dumps('servicecredit_2',servicecredit_2)
        json.dumps('servicecredit_3',servicecredit_3)
        json.dumps('servicecredit_4',servicecredit_4)
        json.dumps('servicecredit_5',servicecredit_5)
        return render(request,'statistics.html',{'al_or':all_orders,'al_co':all_commit,'no_co':not_commit,'d1':desccredit_1,'d2':desccredit_2,'d3':desccredit_3,'d4':desccredit_4,'d5':desccredit_5,'s1':servicecredit_1,'s1':servicecredit_1,'s2':servicecredit_2,'s3':servicecredit_3,'s4':servicecredit_4,'s5':servicecredit_5})
        
        
def friend_link(request):
    return render(request,'link.html',{})
    
def quanlification(request):
    return render(request,'quanlification.html',{})
  
def newhire(request):
	return render_to_response('hire.html',{})
	
def artificial_apeal(request):
	return render_to_response('artificial_apeal.html',{})

def contact_us(request):
	return render_to_response('contact_us.html',{})
	
	
def business_cooperation(request):
    return render(request,'business_cooperation.html',{})

def union_website(request):
    return render(request,'union_website.html',{})


def representations(request):
    return render(request,'representations.html',{})

def safe_center(request):
    return render(request,'safe_center.html',{})

def introduce(request):
    return render(request,'zhengzihui.html',{})

def trustedwebsite(request):
    return render(request,'trustedwebsite.html',{})

#个人注册by cyf
def g_register(request):
    errors = []
    user_name = None
    user_password = None
    user_password2 = None
    user_telephone = None
    user_email = None
    falg = False
    add = []
    if request.method == 'POST':
        if not request.POST.get('_username'):
            errors.append('请输用户名')
        else:
            user_name = request.POST.get('_username')
        if not request.POST.get('_email'):
            errors.append('请输入邮箱')
        else:
            user_email = request.POST.get('_email')
        if not request.POST.get('password'):
            errors.append('请输入密码')
        else:
            user_password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('请重复输入密码')
        else:
            user_password2 = request.POST.get('password2')
        if user_password is not None and user_password2 is not None:
            if user_password == user_password2:
                falg = True
            else:
                errors.append('两次密码输入不一致')
        if not request.POST.get('_telephone'):
            errors.append('请输入电话号码')
        else:
            user_telephone = request.POST.get('_telephone')

        if user_name is not None and user_password is not None and user_telephone is not None and user_email is not None and falg:
            '''自我评价：写的真特么蠢'''
            try:
                user = tb_user.objects.get(user_name = user_name)
                errors.append('用户名已存在')
                return render_to_response('g_register.html',{'errors':errors})
            except tb_user.DoesNotExist:
                pass
            add = tb_user()
            add2 = tb_user_expand()
            add.user_name = user_name
            add.user_password = user_password
            add.user_telephone = user_telephone
            add.user_email = user_email
            add.user_auth = 0
            '''add2.company_name = None
            add2.company_district = None
            add2.company_address = None
            add2.company_registered_capital = None
            add2.company_stuff_no = None
            add2.company_industry = None
            add2.company_nature = None
            add2.companyUserContactName = None
            add2.companyUserPhone = None
            add2.company_tel = None
            add2.company_email = None
            add2.save()
            expand = tb_user_expand.objects.order_by('-user_id')[:1]
            add.expand = expand'''
            add.expand=None
            add.save()
            user_id = add.user_id
            token = token_confirm.generate_validate_token(user_name)
            print(token)
            message = "\n".join([u'{0},欢迎注册政资汇'.format(user_name),u'请访问该链接，完成用户验证(链接1小时内有效):','/'.join(['127.0.0.1:8000','register2',token])])
            #message = '/'.join(['127.0.0.1:8000','register2',token])
            send_mail(u'注册用户验证信息', message, 'changyifan123@qq.com', [user_email])
            
            return render_to_response('register2.html')
    return render_to_response('g_register.html',{'errors':errors})
    



#验证
def register2(request):  
    errors= []  
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('code'):  
            errors.append('请输入验证码')  
        else:  
            code = request.POST.get('code')
        if code is not None:
            user=User.objects.create_user(code)  
            user.is_active=True  
            user.save  
        
        return render_to_response('register3.html')
    return render_to_response('register2.html', {'errors': errors})    

#注册成功 暂时没用到
def register3(request):  
    username = '未定义'
    userid = '0'
    if 'user_name_r3' in request.GET:
        username = request.GET['user_name_r3']
    if 'user_name' in request.session:
        del request.session['user_name']
    request.session['user_name'] = username
    if 'user_id_r3' in request.GET:
        userid = request.GET['user_id_r3']
    
    request.session['user_id'] = userid
    #print(request.session['user_id'])
    #print(request.session['user_name_s'])
    if 'unregist_tobepay_goodsid' in request.session:
        goodsid =request.session['unregist_tobepay_goodsid']
        return HttpResponseRedirect('/selectpay')
    else:
        return render_to_response('denglu.html')  

        

#登陆 by cyf
def login(request):
    a_click_items=[]
    click_items = tb_item_click.objects.order_by('-click_counter')[:4]
    for click_item in click_items:
        a_click_item = {}    
        a_click_item['id'] = click_item.item_id#获取项目id
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga#获取项目资助金额
        item=tb_item.objects.get(item_id=click_item.item_id)
        item_pa_id=item.item_pa_id
        a_click_item['ipa_name'] = tb_item_pa.objects.get(ipa_id=item_pa_id).ipa_name#获取项目管理单位名称
        
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_click_item['item_publish'] = tb_item.objects.get(item_id=click_item.item_id).item_publish.strftime('%Y.%m.%d')#获取项目开始时间
        a_click_item['item_deadtime'] = tb_item.objects.get(item_id=click_item.item_id).item_deadtime.strftime('%Y.%m.%d')#获取项目截止时间
        start_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_click_item['item_consume_time'] = 100
            a_click_item['item_key'] = "已结束"
        else:
            a_click_item['item_consume_time'] = int(consume_time)
        

        a_click_items.append(a_click_item)
    print "testing..."
    print a_click_items
    errors= []  
    user_name=None  
    password=None
    user = tb_user()
    if 'user_name' in request.COOKIES:
        response = render_to_response('index.html',{'user_name':request.COOKIES['user_name']})
        return response
    if 'user_id' in request.COOKIES:
        userid = int(request.COOKIES['user_id'])
        user_name_getby_id = tb_user.objects.get(user_id = userid)
        response = render_to_response('index.html',{'user_name':user_name_getby_id})
        return response
    if request.method == 'POST' :  
        if not request.POST.get('_username'):  
            errors.append('请输入用户名')  
        else:
            user_name = request.POST.get('_username')  
        if not request.POST.get('password'):  
            errors.append('请输入登陆密码')  
        else:  
            password= request.POST.get('password')  
        if user_name is not None and password is not None:
            try:
                user = tb_user.objects.get(user_name = user_name)
            except tb_user.DoesNotExist:
                errors.append('用户名不存在')
            if user.user_auth == 0:
            	errors.append('请查看邮件完成用户认证')
            	return render_to_response('denglu.html', {'errors': errors})
            if password == user.user_password:
                
                response = render_to_response('index.html',{'user_name':user.user_name,'a_click_items':a_click_items})
                
                response.set_cookie('user_name',user_name)
                response.set_cookie('user_id',user.user_id)
                #print(user.expand.company_name)
                #YZ
                if 'unregist_tobepay_goodsid' in request.COOKIES:
                    goodsid = request.COOKIES['unregist_tobepay_goodsid']
                    responsenotpay = HttpResponseRedirect('/service_list/?itemid='+str(goodsid))
                    responsenotpay.set_cookie('user_name',user_name)
                    responsenotpay.set_cookie('user_id',user.user_id)
                    return responsenotpay
                return response
            else:
                errors.append('密码错误')
    return render_to_response('denglu.html', {'errors': errors})
    
def logout(request):
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('user_name')
        response.delete_cookie('user_id')
        return response
def selectpay(request):
	#用户已经登陆，跳到选择支付这一步时自动删除为支付的订单标志
    if 'user_id' in request.COOKIES:
        #goodsid 肯定存在的
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.get(goods_id = service_detail_goods_id)
            response = render(request,'selectpay.html', {'goods':goods})
            if 'unregist_tobepay_goodsid' in request.COOKIES:
                response.delete_cookie('unregist_tobepay_goodsid') 
            return response
	#若未登陆，计入未支付的商品ID号，跳到注册
    else:
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.get(goods_id = service_detail_goods_id)
            response =  HttpResponseRedirect("/regCompany")
            if 'unregist_tobepay_goodsid' in request.COOKIES:
                response.delete_cookie('unregist_tobepay_goodsid') 
            response.set_cookie('unregist_tobepay_goodsid',goods.goods_id)
            #print(request.COOKIES['unregist_tobepay_goodsid'])
        return response

        


#找回密码步骤一
def password1(request):
    errors= []  
    account=None
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('account'):  
            errors.append('请输入用户名')  
        else:  
            account = request.POST.get('account')
        if not request.POST.get('code'):  
            errors.append('请输入图形验证码')  
        else:  
            code = request.POST.get('code')
        if account is not None and code is not None:
            user=User.objects.create_user(account,code)  
            user.is_active=True  
            user.save  
        return HttpResponseRedirect('password2.html')
    return render_to_response('password1.html', {'errors': errors})   

#找回密码步骤二
def password2(request):
    errors= []  
    code=None
    if request.method == 'POST' :  
        if not request.POST.get('code'):  
            errors.append('请输入手机动态密码')  
        else:  
            code = request.POST.get('code')
        if code is not None:
            user=User.objects.create_user(account,code)  
            user.is_active=True  
            user.save  
        return HttpResponseRedirect('password3.html',{})
    return render_to_response('password2.html', {'errors': errors})  

#找回密码步骤三
def password3(request):
    errors= []  
    password=None  
    password2=None
    CompareFlag=False
    if request.method == 'POST':
        if not request.POST.get('password'):  
            errors.append('请输入密码')  
        else:  
            password= request.POST.get('password')  
        if not request.POST.get('password2'):  
            errors.append('请确认密码')  
        else:  
            password2= request.POST.get('password2')  
  
        if password is not None and password2 is not None:  
            if password == password2:  
                CompareFlag = True  
            else:  
                errors.append('两次输入密码不一致，请重新输入 ')   
        if password is not None and password2 is not None and CompareFlag :   
            user=User.objects.create_user(password)  
            user.is_active=True  
            user.save  
            return HttpResponseRedirect('password4.html',{})  
    return render_to_response('password3.html', {'errors': errors})

#找回密码步骤四
def password4(request):   
    return render_to_response('denglu.html',{})             
         
def download(request):
    return render(request,'download.html',{})



#logout by cyf
#def logout(request):
    #return render_to_response('index.html',{})

#激活账户 by cyf
def active_user(request, token):
	errors=[]
	try:
		user_name = token_confirm.confirm_validate_token(token)
	except:
		errors.append('对不起，验证链接已经过期')
		return render_to_response('auth.html',{'errors':errors})
	try:
		user = tb_user.objects.get(user_name = user_name)
	except tb_user.DoesNotExist:
		errors.append('对不起，您所验证的用户不存在，请重新注册')
		return render_to_response('auth.html',{'errors':errors})
	user.user_auth = 1
	user.save()
	return HttpResponseRedirect('/login',{})
		
	


	
'''	#for test
def regCompany(request):
    return render_to_response("regCompany.html")'''
	
	
#正儿八经的企业注册 by cyf

def regCompany(request):
    add = []
    add2 = []
    if request.method == 'POST':
        companyUserName = request.POST.get("regName")
        companyUserPassword = request.POST.get("password")
        companyUserPassword2 = request.POST.get("password2")
        companyUserCompanyName = request.POST.get("companyName")
        companyUserCompanyLocation = request.POST.get("companyLocation")
        companyUserCompanyAddress = request.POST.get("companyAddress")
        companyUserCompanyCapital = request.POST.get("companyCapital")
        companyUserCompanyPeople = request.POST.get("companyPeople")
        companyUserCompanyIndustry = request.POST.get("companyIndustry")
        companyUserCompanyNature = request.POST.get("companyNature")
        companyUserContactName = request.POST.get("contactName")
        companyUserPhone = request.POST.get("phone")
        companyUserTelephone = request.POST.get("telphone")
        companyUserEmail = request.POST.get("email")
        securityCode = request.POST.get("securityCode")
        securityCode2 = request.POST.get("securityCode2")
        try:
            user1 = tb_user.objects.get(user_name = companyUserName)
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("用户名重复！");</script>'})
        except tb_user.DoesNotExist:
            pass
        try:
            user2 = tb_user_expand.objects.get(company_name = companyUserCompanyName)
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("该公司已被注册！");</script>'})
        except tb_user_expand.DoesNotExist:
            pass
        if securityCode != securityCode2:
            return render(request, 'regCompany.html', {'regName': companyUserName,
                                                       'password': companyUserPassword,
                                                       'password2': companyUserPassword2,
                                                       'companyName': companyUserCompanyName,
                                                       'companyLocation': companyUserCompanyLocation,
                                                       'companyAddress': companyUserCompanyAddress,
                                                       'companyCapital': companyUserCompanyCapital,
                                                       'companyPeople': companyUserCompanyPeople,
                                                       'companyIndustry': companyUserCompanyIndustry,
                                                       'companyNature': companyUserCompanyNature,
                                                       'contactName': companyUserContactName, 'phone': companyUserPhone,
                                                       'telphone': companyUserTelephone, 'email': companyUserEmail,
                                                       'securityCode2': securityCode,
                                                       'message': '<script type="text/javascript">alert("短信验证码错误！");</script>'})
        add = tb_user()
        add2 = tb_user_expand()
        add.user_name = request.POST.get("regName")
        add.user_password = request.POST.get("password")
        add.user_telephone = request.POST.get("telphone")
        add.user_email = request.POST.get("email")
        add.user_type = 1
        add.user_auth = 1
        add2.company_name = request.POST.get("companyName")
        add2.company_district = request.POST.get("companyLocation")
        add2.company_address = request.POST.get("companyAddress")
        add2.company_registered_capital = request.POST.get("companyCapital")
        add2.company_stuff_no = request.POST.get("companyPeople")
        add2.company_industry = request.POST.get("companyIndustry")
        add2.company_nature = request.POST.get("companyNature")
        add2.companyUserContactName = request.POST.get("contactName")
        add2.companyUserPhone = request.POST.get("phone")
        add2.company_tel = request.POST.get("telphone")
        add2.company_email = request.POST.get("email")
        add2.save()
        expand = tb_user_expand.objects.get(company_name = companyUserCompanyName)
        add.expand = expand
        add.save()
        return render_to_response("index.html", {})
    return render_to_response("regCompany.html")


#雅致的手机验证，for test，by cyf
def register_sms(request):
    companyUserName = request.POST.get("regName")
    companyUserPassword = request.POST.get("password")
    companyUserPassword2 = request.POST.get("password2")
    companyUserCompanyName = request.POST.get("companyName")
    companyUserCompanyLocation = request.POST.get("companyLocation")
    companyUserCompanyAddress = request.POST.get("companyAddress")
    companyUserCompanyCapital = request.POST.get("companyCapital")
    companyUserCompanyPeople = request.POST.get("companyPeople")
    companyUserCompanyIndustry = request.POST.get("companyIndustry")
    companyUserCompanyNature = request.POST.get("companyNature")
    companyUserContactName = request.POST.get("contactName")
    companyUserPhone = request.POST.get("phone")
    companyUserTelephone = request.POST.get("telphone")
    companyUserEmail = request.POST.get("email")
    securityCode=random.randint(1000, 9999)
    req=top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey,secret))

    req.extend="123456"
    req.sms_type="normal"
    req.sms_free_sign_name="身份验证"
    req.sms_param='{"code":"%d","product":"雅峙"}'%(securityCode)
    req.rec_num=companyUserTelephone
    req.sms_template_code="SMS_4465526"
    try:
	    resp= req.getResponse()
	    print(resp)
    except Exception,e:
	    print(e)
	    return HttpResponse("sms error!")
    finally:
	    return render(request,'regCompany.html',{'regName':companyUserName, 'password':companyUserPassword, 'password2':companyUserPassword2, 'companyName':companyUserCompanyName, 'companyLocation':companyUserCompanyLocation, 'companyAddress':companyUserCompanyAddress, 'companyCapital':companyUserCompanyCapital, 'companyPeople':companyUserCompanyPeople, 'companyIndustry':companyUserCompanyIndustry, 'companyNature':companyUserCompanyNature, 'contactName':companyUserContactName, 'phone':companyUserPhone, 'telphone':companyUserTelephone, 'email':companyUserEmail, 'securityCode2':securityCode, 'message':'<script type="text/javascript">alert("验证码已发送！");</script>'})





'''
**************
商家后台部分
**************
'''







def bus_comment_manager(request):
    service_provider = 'cyf'
    comment_list = tb_goods_evaluation.objects.filter(service_provider=service_provider)
   # print(comment_list)
    #print service_provider
    return render_to_response("bus_comment_manager.html", {'comment_list':comment_list})

def service_provider_reply(request):
    if request.GET['id']:
        id = request.GET['id']
        goods = tb_goods_evaluation.objects.get(goods_id=id)
        user_name = goods.user_name
        if request.method == 'POST':
            goods.reply_content = request.POST.get("reply")
            goods.save()
            return HttpResponseRedirect('/busindex',{})
    return render_to_response('service_provider_reply.html', {'user_name':user_name})



def info_main(request):
    return render_to_response('info_main.html', {})











#订单管理-查看详情  lqx  
def bw_order_manage_detail(request):
    order_no = request.GET['id']
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = tb_order.objects.filter(sp_id=sp_id,order_no=order_no)#查看订单根据订单编号显示
    merchant=tb_service_provider.objects.filter(sp_id=sp_id)#查看订单商家
    
    for order in all_order:

        # print order.goods_id
        temp_order = tb_goods.objects.get(goods_id=order.goods_id)
        temp_buyer = tb_user.objects.get(user_id=order.buyer_id)
        temp_sptype =tb_service_provider.objects.get(sp_id=order.sp_id).sp_type##服务类型
        temp_stime= tb_balist.objects.get(order_no=order.order_no).ba_time
        #print temp_stime
        temp_ftime= tb_balist.objects.get(order_no=order.order_no).ba_ftime
        if temp_buyer.expand_id:

            temp_buyer_expand = tb_user_expand.objects.get(user_id=order.buyer_id)
            buyer_expand_address = temp_buyer_expand.company_address
            buyer_expand_tel=temp_buyer_expand.company_tel
            #print buyer_expand_address

            if buyer_expand_address == '':
                buyer_expand_address == '该用户所在公司还未完善地址信息 '
            buyer_expand_contact = temp_buyer_expand.companyUserContactName
            if buyer_expand_contact == '':
                buyer_expand_contact = '该用户所在公司还未指定联系人'
        else:
            buyer_expand_address = "用户还未填写,请电话联系"
            buyer_expand_contact = temp_buyer.user_name
        goods_name = temp_order.goods_name
        goods_code = temp_order.goods_code
        goods_pay =temp_order.goods_pay
        if order.efile_send:
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'
        # 添加的三个属性
        order.goods_name = goods_name
        order.goods_code = goods_code#服务产品编号 
        order.goods_pay = goods_pay#服务价格
        order.buyer_expand_address = str(buyer_expand_address)
        order.buyer_expand_contact = str(buyer_expand_contact)
        order.buyer_expand_tel = str(buyer_expand_tel)
        order.sptype = temp_sptype
        order.stime = temp_stime#商家交单时间
        order.ftime = temp_ftime#平台交单时间
        ##lqx判断服务类型
        if order.sptype=='申报服务提供商':
            order.s_type='项目申报'
        elif order.sptype=='项目申报配套服务工商代办'|'项目申报配套服务资质代办'|'项目申报配套服务知识产权'|'项目申报配套服务财务服务':
            order.s_type='配套服务'
        else:
            order.s_type='融资服务'
        order.s_type=str(order.s_type) 

    return render(request, "bw_order_manage_detail.html", {'all_order': all_order, 'sp_id': sp_id,'merchant':merchant})
    
#申请加盟BY jianuo
def applyforjoin(request):	
    add = []
    sp_type=""
    
    if request.method == 'POST':
        flag = request.POST.get("flag")
        myflag=str(flag)
        #print myflag
        sp_name = request.POST.get("sp_name")
        con_name = request.POST.get("con_name")
        tel = request.POST.get("tel")
        email = request.POST.get("email")
        sp_type1= request.POST.get("sp_type1","")
        sp_type2= request.POST.get("sp_type2","")
        sp_type3= request.POST.get("sp_type3","")
        if myflag == "1":
          sp_type=sp_type1
        if myflag=="2":
          sp_type=sp_type1+"+"+sp_type2
        if myflag=="3":
          sp_type=sp_type1+"+"+sp_type3
        
        print sp_type

        

        


        add = tb_service_provider()
       
        add.tel = request.POST.get("tel")
        add.email = request.POST.get("email")
        add.sp_name = request.POST.get("sp_name")
        add.con_name = request.POST.get("con_name")
        add.sp_type =sp_type
        #add by yz

        

        sp_code = random.randint(0, 1000000)
        while (len(tb_service_provider.objects.filter(sp_code =sp_code)) == 1):
            sp_code = random.randint(0, 1000000)
        add.sp_code = sp_code
        add.psw = '000000'

        add.sp_auth =0#默认值\
        add.master ='000'#默认值\
        add.sp_image1 ='000'
        add.sp_image2 ='000'
        add.sp_grade =00#默认值\
        add.sp_sort=00#默认值
        add.area_id='00'
        add.Register_cap =00
        add.staff_number =00
        add.Annual_totals =00
        add.organization_name ='00'
        add.organization_id =00
        add.organization_assets =00
        add.organization_profile ='000'
        add.is_recommend =0
		
		

        add.save()
        return render_to_response("success.html", {})
    return render_to_response("applyforjoin.html",{})
def success(request):
    return render_to_response("success.html",{})


def balfororders(request):
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    all_order = get_all_order_of_sp(sp_id)
    filter_order=[]

    sp_type=request.GET.get('sp_type')
    sp_type1=None
    sp_type2=None
    sp_type3=None
    if sp_type=="项目申报":
        sp_type1=True
        
        #all_order=all_order[:3]
        
    elif sp_type=="配套服务":
        sp_type2=True
        #all_order=all_order[:2]
    else:
        sp_type3=True
        #all_order=all_order[:3]
    
    
    for order in all_order:

        if order.efile_send :
            order.str_efile_send = '已经交付'
        else:
            order.str_efile_send = '未交付'
        if order.paper_send:
            order.str_paper_send = '已经送达'
        else:
            order.str_paper_send = '未送达'
            
        ##lqx判断服务类型
        if order.sptype=='申报服务提供商':
            order.s_type='项目申报'
        elif order.sptype=='项目申报配套服务工商代办'|'项目申报配套服务资质代办'|'项目申报配套服务知识产权'|'项目申报配套服务财务服务':
            order.s_type='配套服务'
        else:
            order.s_type='融资服务'
        order.s_type=str(order.s_type)   
        
    #print sp_type
    
    if sp_type=='项目申报':
        for order in all_order:
           print order.sptype
           if order.sptype=='申报服务提供商':
              filter_order.append(order)
      
    print len(filter_order)
    
    return render(request,"balfororders.html",{'all_order':filter_order,'sp_id':sp_id,"sp_type1":sp_type1,"sp_type2":sp_type2,"sp_type3":sp_type3,"sp_type":sp_type,'order.buyer_name':order.buyer_name})  
          
        


def b_work_comment_manager(request):
    if 'area' not in request.COOKIES:
        comment_list = tb_goods_evaluation.objects.all()
    else:
        area = request.COOKIES['area']
        print(area)
        if area == '0':
            comment_list = tb_goods_evaluation.objects.filter(location = '成都')
        else:
            comment_list = tb_goods_evaluation.objects.exclude(location = '成都')


    return render_to_response("b_work_comment_manager.html", {'comment_list': comment_list})
#项目管理by jianuo
def bus_project_management(request):
    if 'sp_id' in request.COOKIES:

        sp_id = request.COOKIES['sp_id']
    else:




        sp_id = 1
    a_click_items=[]
    click_items = tb_item_click.objects.order_by('-click_counter')[:4]
    for click_item in click_items:
        a_click_item = {}    
        a_click_item['id'] = click_item.item_id#获取项目id
        a_click_item['item_code']=tb_item.objects.get(item_id=click_item.item_id).item_code#获取项目编号
        a_click_item['name'] = (tb_item.objects.get(item_id=click_item.item_id)).item_name#获取项目名字
        album = tb_album.objects.filter(album_type=0,affiliation_id=click_item.item_id,is_default=1).order_by('-nacl_sort')[0]#获取项目对应的相册id
        album_id = album.album_id
        a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]#获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
        a_click_item['item_ga'] = tb_item.objects.get(item_id=click_item.item_id).item_ga#获取项目资助金额
        item=tb_item.objects.get(item_id=click_item.item_id)
        item_pa_id=item.item_pa_id
        a_click_item['ipa_name'] = tb_item_pa.objects.get(ipa_id=item_pa_id).ipa_name#获取项目管理单位名称
        a_click_item['item_url']=tb_item.objects.get(item_id=click_item.item_id).item_url#获取原文链接
        now_seconds = time.time() - 8*60*60  #距离1970的秒数  将东八区转换为0时区
        a_click_item['item_publish'] = tb_item.objects.get(item_id=click_item.item_id).item_publish.strftime('%Y.%m.%d')#获取项目开始时间
        a_click_item['item_deadtime'] = tb_item.objects.get(item_id=click_item.item_id).item_deadtime.strftime('%Y.%m.%d')#获取项目截止时间
        start_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_publish.timetuple())  #utc 0时区
        end_seconds = time.mktime(tb_item.objects.get(item_id=click_item.item_id).item_deadtime.timetuple())
        consume_time = (now_seconds-start_seconds)/(end_seconds-start_seconds)*100
        if consume_time > 100:
            a_click_item['item_consume_time'] = 100
            a_click_item['item_key'] = "已结束"
        else:

            a_click_item['item_consume_time'] = int(consume_time)
        

        a_click_items.append(a_click_item)

    return render_to_response("bus_project_management.html",{'a_click_items':a_click_items})
	
#项目管理详情 by jianuo
def bpm_details(request):
    bpm_id=request.GET['id']
    a_click_items=[]
    a_shoucang_items=[]
    a_shoucang_goods=[]
    a_fuwus=[]
    if 'sp_id' in request.COOKIES:
        sp_id = request.COOKIES['sp_id']
    else:
        sp_id = 1
    items = tb_item.objects.get(item_id=bpm_id)#item表   
    item_pa_id=items.item_pa_id
    item_pa = tb_item_pa.objects.get(ipa_id=item_pa_id)#item_pa表
    s_lists=tb_shoucang_item.objects.filter(item_id=bpm_id)#客户收藏
    sb_lists=tb_shoucang_goods.objects.filter(goods_id=bpm_id)#客户申报
    fw_lists=tb_goods.objects.filter(item_id=bpm_id)#提供服务
    shoucang_items = tb_shoucang_item.objects.filter(item_id=bpm_id)[:4]
    for shoucang_item in shoucang_items:
        a_shoucang_item = {}    
        a_shoucang_item['user_name']=tb_user.objects.get(user_id=shoucang_item.user_id).user_name
        a_shoucang_item['company_address']=tb_user_expand.objects.get(user_id=shoucang_item.user_id).company_address
        a_shoucang_item['companyUserContactName']=tb_user_expand.objects.get(user_id=shoucang_item.user_id).companyUserContactName
        a_shoucang_item['companyUserPhone']=tb_user_expand.objects.get(user_id=shoucang_item.user_id).companyUserPhone
        a_shoucang_items.append(a_shoucang_item)
    shoucang_goods = tb_shoucang_goods.objects.filter(goods_id=bpm_id)[:4]
    for shoucang_good in shoucang_goods:
        a_shoucang_good = {}    
        a_shoucang_good['user_name']=tb_user.objects.get(user_id=shoucang_good.user_id).user_name
        a_shoucang_good['company_address']=tb_user_expand.objects.get(user_id=shoucang_good.user_id).company_address
        a_shoucang_good['companyUserContactName']=tb_user_expand.objects.get(user_id=shoucang_good.user_id).companyUserContactName
        a_shoucang_good['companyUserPhone']=tb_user_expand.objects.get(user_id=shoucang_good.user_id).companyUserPhone
        a_shoucang_goods.append(a_shoucang_good)
    fuwus=tb_goods.objects.filter(item_id=bpm_id)[:4]
    for fuwu in fuwus:
        a_fuwu={}
        sps=tb_service_provider.objects.get(sp_id=fuwu.sp_id)
        sp_sp_id=sps.sp_id
        a_fuwu['sp_name']=tb_service_provider.objects.get(sp_id=sp_sp_id).sp_name
        a_fuwu['area_id']=tb_service_provider.objects.get(sp_id=sp_sp_id).area_id
        a_fuwu['con_name']=tb_service_provider.objects.get(sp_id=sp_sp_id).con_name
        a_fuwu['tel']=tb_service_provider.objects.get(sp_id=sp_sp_id).tel
        a_fuwus.append(a_fuwu)
    return render_to_response("bpm_details.html",{'items':items,'size':len(s_lists),'size1':len(sb_lists),'a_shoucang_items':a_shoucang_items,'a_shoucang_goods':a_shoucang_goods,'a_fuwus':a_fuwus,'item_pa':item_pa,'size2':len(fw_lists)})


# 用于政资信息共享
def shareinformation(request):
    if request.method == "POST":
        form = ShareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/Publish/')
    else:
        form = ShareForm()
    return render(request, 'shareinformation.html', {'form': form})


# 用于发布人信息发布
def Publish(request):
    if request.method == "POST":
        form2 = LinkerForm(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'SharePublish.html', {'post': post})
    else:
        form2 = LinkerForm()
    return render(request, 'sharedetail.html', {'form2': form2})


flag = True


def change(request):
    global flag, link
    if flag:
        id1 = int(request.GET['id'])
        link = Linker.objects.get(id=id1)
        flag = False
        return render_to_response('sharedetail.html', {'link': link})
    else:

        Linker.linkname = request.GET['linkname']
        Linker.linktephon = request.GET['linktelphon']
        Linker.linkemail = request.GET['linkemail']
        Linker.linkadress = request.GET['linkadress']
        Linker.remarks = request.GET['remarks']
        Linker.secert = request.GET['secert']
        Linker.save()
        flag = True
        return render_to_response('SharePublish.html', {'right': True})
