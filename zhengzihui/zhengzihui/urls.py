#coding:utf-8
"""zhengzihui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','zhengzihui_app.views.index',name='index'),
    url(r'^hire/$','zhengzihui_app.views.newhire',name='newhire'),
    url(r'^search/$','zhengzihui_app.views.Searchgoods',name='Searchgoods'),
    
    #zss 二级页面
    url(r'^search_result/$','zhengzihui_app.views.search_result',name='search_result'),
    url(r'^search_result_sort_starttime/$','zhengzihui_app.views.search_result_sort_starttime',name='search_result_sort_starttime'),
    url(r'^search_result_sort_deadtime/$','zhengzihui_app.views.search_result_sort_deadtime',name='search_result_sort_deadtime'),
    url(r'^search_result_load/$','zhengzihui_app.views.search_result_load',name='search_result_load'),#用来干嘛的？？
    url(r'^filter_labels/$','zhengzihui_app.views.filter_labels',name='filter_labels'),#当用户选择了筛选条件之后，将值传到主页，再次跳到主页
      
    
    url(r'^project_detail/$','zhengzihui_app.views.project_detail',name='project_detail'),#当有id传入，可显示项目的相关信息
    
    #url(r'^zhengzihui_app/', include('zhengzihui_app.urls')),
    
    url(r'^service_details/$','zhengzihui_app.views.service_details',name="service_details"),
    
    
    url(r'^service_list/$','zhengzihui_app.views.service_list',name="service_list"),
    
    url(r'^pay/', "zhengzihui_app.views.pay",name="pay"),

    
#用户中心
    url(r'^zzh/user_center/', "zhengzihui_app.views.user_center",name="user_center"),
    
    #用户信息
        #我的信息
    url(r'^zzh/my_info/', "zhengzihui_app.views.my_info",name="my_info"),
        #保存修改信息
    url(r'^zzh/modify_user/', "zhengzihui_app.views.modify_user",name="modify_user"),
        #安全中心
    url(r'^zzh/safe_center/', "zhengzihui_app.views.safe_center",name="safe_center"),
        #支付绑定
    url(r'^zzh/pay_combine/', "zhengzihui_app.views.pay_combine",name="pay_combine"),
        #等级与成长
    url(r'^zzh/grade_grow/', "zhengzihui_app.views.grade_grow",name="grade_grow"),


    #订单管理
        #全部订单
    url(r'^zzh/all_orders/', "zhengzihui_app.views.all_orders",name="all_orders"),
        #未支付
    url(r'^zzh/not_pay/', "zhengzihui_app.views.not_pay",name="not_pay"),
        #已支付
    url(r'^zzh/payed/', "zhengzihui_app.views.payed",name="payed"),
       #已发货
    url(r'^zzh/delivered/', "zhengzihui_app.views.delivered",name="delivered"),
       #已验收
    url(r'^zzh/checked/', "zhengzihui_app.views.checked",name="checked"),
       #已取消
    url(r'^zzh/delete/', "zhengzihui_app.views.delete",name="delete"),


    #评价管理
        #全部评价
    url(r'^zzh/all_evaluations/', "zhengzihui_app.views.all_evaluations",name="all_evaluations"),
        #未评论
    url(r'^zzh/not_evaluate/', "zhengzihui_app.views.not_evaluate",name="not_evaluate"),
        #已评论
    url(r'^zzh/evaluated/', "zhengzihui_app.views.evaluated",name="evaluated"),
    
    #主页底部链接页面部分 友情链接
    url(r'^friend_link',"zhengzihui_app.views.friend_link",name="friend_link"),
    url(r'^quanlification',"zhengzihui_app.views.quanlification",name="quanlification"),
]
