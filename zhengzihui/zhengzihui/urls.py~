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
    url(r'^zzh_ajax/$','zhengzihui_app.views.ajax',name='ajax'),
    url(r'^zzh_filter/$','zhengzihui_app.views.filter',name='filter'),
    url(r'^hello/$','zhengzihui_app.views.hello',name = 'hello'),
]
