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
    url(r'^zzh_index/$','zhengzihui_app.views.ind',name='ind'),
    url(r'^index/$','zhengzihui_app.views.index',name='index'),
    url(r'^search/$','zhengzihui_app.views.Searchgoods',name='Searchgoods'),
    
    url(r'^zzh_ajax/$','zhengzihui_app.views.ajax',name='ajax'),#用来干嘛的？？
    
    url(r'^zzh_filter/$','zhengzihui_app.views.filter',name='filter'),#当用户选择了筛选条件之后，将值传到主页，再次跳到主页
    
    url(r'^item_details/$','zhengzihui_app.views.item_details',name = 'item_details'),#当有id传入，可显示项目的相关信息
    
    #url(r'^zhengzihui_app/', include('zhengzihui_app.urls')),
    
    url(r'^service_details/$','zhengzihui_app.views.service_details',name="service_details"),
    
    
    url(r'^service_list/$','zhengzihui_app.views.service_list',name="service_list"),
    
    url(r'^pay/', "zhengzihui_app.views.pay",name="pay"),
    url(r'^create_test_data/$','zhengzihui_app.views.create_test_data',name='create_test_data'),
    url(r'^project_detail/$','zhengzihui_app.views.project_detail',name='project_detail'),
]
