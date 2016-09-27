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
import zhengzihui_app.views
from urls import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
   
    ########################排序

    url(r'^item_sortbyLevel',zhengzihui_app.views.item_sortbyLevel,name='item_sortbyLevel'),
    url(r'^item_sortbyComprihensive',zhengzihui_app.views.item_sortbyComprihensive,name='item_sortbyComprihensive'),
    url(r'^search_result_sort_deadtime/$',zhengzihui_app.views.search_result_sort_deadtime,name='search_result_sort_deadtime'),
    
    
    
    url(r'^search_result_load/$',zhengzihui_app.views.search_result_load,name='search_result_load'),
    url(r'^filter_labels/$',zhengzihui_app.views.filter_labels,name='filter_labels'),#当用户选择了筛选条件之后，将值传到主页，再次跳到主页
    #修复从搜索结果界面获得到 item_details/ url的bug,并没有写，但是出现了      
    url(r'^item_details/$','zhengzihui_app.views.item_details',name='item_details'),#当有id传入，可显示项目的相关信息
    url(r'^project_detail/$',zhengzihui_app.views.project_detail,name='project_detail'),#当有id传入，可显示项目的相关信息
    

    #下面是服务商的三种排序方式
    url(r'^sortServByComp/$',zhengzihui_app.views.sortServByComp,name="sortServByComp"),
    url(r'^sortServBypayahead/$',zhengzihui_app.views.sortServBypayahead,name="sortServBypayahead"),
    url(r'^sortServByaward/$',zhengzihui_app.views.sortServByaward,name="sortServByaward"),
    url(r'^service_details/$',zhengzihui_app.views.service_details,name="service_details"),
    url(r'^service_list/$',zhengzihui_app.views.service_list,name="service_list"),

    #预定流程
    url(r'^contact_details/$',zhengzihui_app.views.contact_details,name="contact_details"),
    url(r'^order_details/$',zhengzihui_app.views.order_details,name="order_details"),
    url(r'^order_completed/$',zhengzihui_app.views.order_completed,name="order_completed"),
    url(r'^pay/', zhengzihui_app.views.pay,name="pay"),
    url(r'^shoucang_item/',zhengzihui_app.views.shoucang_item,name="shoucang_item"),
    url(r'^shoucang_goods/',zhengzihui_app.views.shoucang_goods,name="shoucang_goods"),

   
    

#用户中心

	
	#收藏管理
		#收藏的项目
	url(r'^zzh/collects/', zhengzihui_app.views.collects,name="collects"),
		#收藏的服务
    url(r'^zzh/collect_sever/', zhengzihui_app.views.collect_serve,name="collect_serve"),
		
		

    #主页底部链接页面部分 友情链接
    url(r'^friend_link',zhengzihui_app.views.friend_link,name="friend_link"),
    #政资汇简介
    url(r'^introduce',zhengzihui_app.views.introduce,name="introduce"),
  

     #登陆注册
    url(r'^login/$', zhengzihui_app.views.login,name='login'),
    url(r'^logout/$',zhengzihui_app.views.logout,name='logout'),
   

    
    





   
	#商家入住首页
	url(r'^busindex/$',zhengzihui_app.views.busindex,name='busindex'),
	url(r'^buspubservice/',zhengzihui_app.views.buspubservice,name='buspubservice'),
	
    #YZ
    url(r'^bus_order_manage/',zhengzihui_app.views.bus_order_manage,name="bus_order_manage"),
    url(r'^bus_counter_manage/',zhengzihui_app.views.bus_counter_manage,name="bus_counter_manage"),
    url(r'^change_paper_send_state/',zhengzihui_app.views.change_paper_send_state,name="change_paper_send_state"),
    url(r'^change_has_pay_state/',zhengzihui_app.views.change_has_pay_state,name="change_has_pay_state"),
    url(r'^sort_has_pay/',zhengzihui_app.views.sort_has_pay,name="sort_has_pay"),
    url(r'^sort_order_manage/',zhengzihui_app.views.sort_order_manage,name="sort_order_manage"),
    url(r'^busindex_sub/$',zhengzihui_app.views.busindex_sub,name='busindex_sub'),
	


]


