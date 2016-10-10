
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
from cyf_views import *
from lqx_views import *
from jianuo_views import *
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
    print keys
    if 'bumen_class1' in request.GET:

        request.session['bumen'] = keys

    if 'bumen_class2' in request.GET:

        request.session['bumen'] = keys
    if 'bumen_class3' in request.GET:

        request.session['bumen'] = keys
    if 'bumen_class4' in request.GET:

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
            album = tb_album.objects.filter(album_type=0, affiliation_id=click_item.item_id, is_default=1).order_by('-nacl_sort')  # 获取项目对应的相册id
            if len(album):

                album_id = album[0].album_id
                a_click_item['pic_url'] = tb_pic.objects.filter(album_id=album_id).order_by('-pic_id')[0].pic_object.url[14:]  # 获得最大pic_id的图片 切片14是去除前缀zhengzihui_app 否则图片不能显示
            else:
                a_click_item['pic_url'] ='/static/images/12.png'
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

        



def selectpay(request):
	#用户已经登陆，跳到选择支付这一步时自动删除为支付的订单标志
    if 'user_id' in request.COOKIES:
        #goodsid 肯定存在的
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.filter(goods_id = service_detail_goods_id)
            if len(goods):
                goods=goods[0]
            else:
                return HttpResponse('该项目暂时还没有服务商，您可以收藏该项目！')
            response = render(request,'selectpay.html', {'goods':goods})
            if 'unregist_tobepay_goodsid' in request.COOKIES:
                response.delete_cookie('unregist_tobepay_goodsid') 
            return response
	#若未登陆，计入未支付的商品ID号，跳到注册
    else:
        if request.GET['goodsid']:
            service_detail_goods_id = request.GET['goodsid']
            goods = tb_goods.objects.filter(goods_id = service_detail_goods_id)
            if len(goods):
                goods=goods[0]
            else:
                return HttpResponse('你还未登陆，请登录。且您访问的项目暂时还没有服务商提供服务！')
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






def info_main(request):
    return render_to_response('info_main.html', {})





def busmaservice(request):
	sp_id=1
	#if 'user_id' in request.COOKIES:
	#	sp_id=request.COOKIES['user_id']
	goods = tb_goods.objects.filter(sp_id=sp_id)
	return render_to_response("busmaservice.html",{'goods_list':goods,})
	


	
def merge_service_details(request):
	sp_id=9
	#if 'user_id' in request.COOKIES:
	#	sp_id=request.COOKIES['user_id']
	if (request.method=="GET"):
		mid=request.GET.get("goodsid")
		#print (mid)
		goods=tb_goods.objects.get(goods_id=mid)
		return render_to_response("busmerservice.html",{'goods':goods})
	else:
		did=request.POST.get("deletegoodsid")
		dgoods=tb_goods.objects.get(goods_id=did)
		dgoods.goods_show=0
		dgoods.goods_status=0
		dgoods.save()
		mod=""
		fea=""
		payt=0
		payth=0
		pay=request.POST.get("pay")
		if(request.POST.get("modon")):
			mod+=request.POST.get("modon")
			pay=request.POST.get("paya")
		if(request.POST.get("modtw")):
			mod+=request.POST.get("modtw")
			payt=request.POST.get("payb")
		if(request.POST.get("modth")):
			mod+=request.POST.get("modth")
			payth=request.POST.get("payc")
		#print(mod)
		if(request.POST.get("feaon")):
			fea+=request.POST.get("feaon")
			fea+="  "
		if(request.POST.get("featw")):
			fea+=request.POST.get("featw")
			fea+="  "
		if(request.POST.get("feath")):
			fea+=request.POST.get("feath")
			fea+="  "
		if(request.POST.get("feafo")):
			fea+=request.POST.get("feafo")
			fea+="  "
		if(request.POST.get("feafi")):
			fea+=request.POST.get("feafi")
			fea+="  "
		#print(fea)
		pay=request.POST.get("paya")
		sname=request.POST.get("sname")
		#payt=request.POST.get("payb")
		fuwuneirong=request.POST.get("fuwuneirong")
		fuwuliucheng=request.POST.get("fuwuliucheng")
		chenggonganli=request.POST.get("chenggonganli")
		fanli=request.POST.get("fanli")
		add=tb_goods_wfc()
		add.goods_payahead=pay
		add.goods_awardmid=payt
		add.goods_awardafter=payth
		add.goods_name=sname
		add.item_id=1
		add.sp_id=sp_id
		add.goods_fanli=fanli
		add.fea=fea
		add.cont=fuwuneirong
		add.steps=fuwuliucheng
		add.exa=chenggonganli
		add.smod=mod
		add.save()
        #print(111)
		return render_to_response("buswaitforchecked.html",{})



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


def ba_for_merchant_supervisor(request):
	"""后台管理的商家管理支线 add by zp.
	"""
	# filter
	if 'order' not in request.COOKIES:
		kind = "ascending_order"
	else:
		kind = request.COOKIES['order']

	# order
        all_list = []
	if kind=="ascending_order":
		all_list = tb_ba_for_merchant_superivisor.objects.all().order_by("-num_of_orders")
	else:
		all_list = tb_ba_for_merchant_superivisor.objects.all().order_by("num_of_orders")

	# sort
	lis = []
	for i in all_list:
		item = {}
		item['merchant_id']=i.merchant_id
		item['merchant_name']=i.merchant_name
		item['merchant_addr']=i.merchant_addr
		item['merchant_linkman']=i.merchant_linkman
		item['phone_num']=i.phone_num
		item['num_of_orders']=i.num_of_orders
		item['merchant_addr']=i.merchant_addr
		item['transaction_amount']=i.transaction_amount
		lis.append(item)

	return render_to_response("balformerchantsupervisor.html",{'lis':lis})


def bw_merchantsupervisor_detail(request):
	"""后台管理的商家管理支线 add by zp.
	"""
	item_id = request.GET.get('id')
	item = tb_ba_for_merchant_superivisor.objects.get(merchant_id=item_id)
	res = {}
	res['merchant_id'] = item.merchant_id
	res['merchant_name'] = item.merchant_name
	res['merchant_addr'] = item.merchant_addr
	res['merchant_linkman'] = item.merchant_linkman
	res['phone_num'] = item.phone_num
	res['num_of_orders'] = item.num_of_orders
	res['transaction_amount'] = item.transaction_amount

	return render_to_response("bw_merchantsupervisor_detail.html",{'res':res})



