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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',zhengzihui_app.views.index,name='index'),
    url(r'^hire/$',zhengzihui_app.views.newhire,name='newhire'),
    url(r'^search/$',zhengzihui_app.views.Searchgoods,name='Searchgoods'),
    
    url(r'^payok/$',zhengzihui_app.views.Payback,name='payok'),
    #zss 二级页面
    url(r'^search_result/$',zhengzihui_app.views.search_result,name='search_result'),
    
    ########################排序
    #url(r'^search_result_sort_starttime/$','zhengzihui_app.views.search_result_sort_starttime',name='search_result_sort_starttime'),
    url(r'^item_sortbyLevel',zhengzihui_app.views.item_sortbyLevel,name='item_sortbyLevel'),
    url(r'^item_sortbyComprihensive',zhengzihui_app.views.item_sortbyComprihensive,name='item_sortbyComprihensive'),
    url(r'^search_result_sort_deadtime/$',zhengzihui_app.views.search_result_sort_deadtime,name='search_result_sort_deadtime'),
    
    
    
    url(r'^search_result_load/$',zhengzihui_app.views.search_result_load,name='search_result_load'),#用来干嘛的？？
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

    url(r'^searchforc/', zhengzihui_app.views.tag_autocomplete,name='auto'),
    

#用户中心
    url(r'^zzh/user_center/', zhengzihui_app.views.user_center,name="user_center"),
    
    #用户信息
        #我的信息
    url(r'^zzh/my_info/', zhengzihui_app.views.my_info,name="my_info"),
    #总览
    #url(r'^zzh/view_all/', "zhengzihui_app.views.view_all",name="view_all"),
        #保存修改信息
    url(r'^zzh/modify_user/', zhengzihui_app.views.modify_user,name="modify_user"),
        #安全中心
    url(r'^zzh/safe_center/', zhengzihui_app.views.safe_center,name="safe_center"),
        #支付绑定
    url(r'^zzh/pay_combine/', zhengzihui_app.views.pay_combine,name="pay_combine"),
        #等级与成长
    url(r'^zzh/grade_grow/', zhengzihui_app.views.grade_grow,name="grade_grow"),


    #订单管理
        #全部订单
    url(r'^zzh/all_orders/', zhengzihui_app.views.all_orders,name="all_orders"),
        #未支付
    url(r'^zzh/not_pay/', zhengzihui_app.views.not_pay,name="not_pay"),
        #已支付
    url(r'^zzh/payed/', zhengzihui_app.views.payed,name="payed"),
       #已发货
    url(r'^zzh/delivered/', zhengzihui_app.views.delivered,name="delivered"),
       #已验收
    url(r'^zzh/checked/', zhengzihui_app.views.checked,name="checked"),
       #已取消
    url(r'^zzh/delete/', zhengzihui_app.views.delete,name="delete"),

       #确认订单
    url(r'^order_enter/', zhengzihui_app.views.order_enter,name="order_enter"),
       #取消订单
    url(r'^order_giveup/', zhengzihui_app.views.order_giveup,name="order_giveup"),
       #删除订单
    url(r'^order_delete/', zhengzihui_app.views.order_delete,name="order_delete"),
       #点击评论按钮
    url(r'^order_commit/', zhengzihui_app.views.order_commit,name="order_commit"),
       #添加评论
    url(r'^order_add_commit/', zhengzihui_app.views.order_add_commit,name="order_add_commit"),
	
	
	#收藏管理
		#收藏的项目
	url(r'^zzh/collects/', zhengzihui_app.views.collects,name="collects"),
		#收藏的服务
    url(r'^zzh/collect_sever/', zhengzihui_app.views.collect_serve,name="collect_serve"),
		
		
    #评价管理
        #我的评价
    url(r'^zzh/my_evaluate/', zhengzihui_app.views.my_evaluate,name="my_evaluate"),
        #评价统计
    url(r'^zzh/statistics/', zhengzihui_app.views.statistics,name="statistics"),
    
    
    #主页底部链接页面部分 友情链接
    url(r'^friend_link',zhengzihui_app.views.friend_link,name="friend_link"),
    url(r'^quanlification',zhengzihui_app.views.quanlification,name="quanlification"),
    #人工申诉
    url(r'^artificial_apeal',zhengzihui_app.views.artificial_apeal,name="artificial_apeal"),
    #联系我们
    url(r'^contact_us',zhengzihui_app.views.contact_us,name="contact_us"),
    #商业合作
    url(r'^business_cooperation',zhengzihui_app.views.business_cooperation,name="business_cooperation"),
    #网站联盟
    url(r'^union_website',zhengzihui_app.views.union_website,name="union_website"),
    #帐号申述
    url(r'^representations',zhengzihui_app.views.representations,name="representations"),
    #政资汇简介
    url(r'^introduce',zhengzihui_app.views.introduce,name="introduce"),
    #可信网站
    url(r'^trustedwebsite',zhengzihui_app.views.trustedwebsite,name="trustedwebsite"),


     #登陆注册
    url(r'^login/$', zhengzihui_app.views.login,name='login'),
    url(r'^logout/$',zhengzihui_app.views.logout,name='logout'),
    url(r'^g_register/$', zhengzihui_app.views.g_register,name='g_register'),
    url(r'^regCompany/$', zhengzihui_app.views.regCompany,name='regCompany'),
    url(r'^register2/$', zhengzihui_app.views.register2,name='register2'),
    url(r'^register3/$', zhengzihui_app.views.register3,name='register3'),
    url(r'^password1/$', zhengzihui_app.views.password1,name='password1'),
    url(r'^password2/$', zhengzihui_app.views.password2,name='password2'),
    url(r'^password3/$', zhengzihui_app.views.password3,name='password3'),
    url(r'^password4/$', zhengzihui_app.views.password4,name='password4'),

    #短信验证页
    url(r'^register_sms/$', zhengzihui_app.views.register_sms, name='register_sms'),
#    企业画像
    url(r'^custom/$', zhengzihui_app.views.custom,name='custom'),
    url(r'savec/$', zhengzihui_app.views.savec,name='savec'),
    url(r'custmap/$', zhengzihui_app.views.cmap,name='cmap'),


    #app下载
    url(r'^download/$', zhengzihui_app.views.download,name='download'),
    #支付选择页面
	url(r'^selectpay/$', zhengzihui_app.views.selectpay,name='selectpay'),
	#邮箱验证页
	url(r'^register2/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',zhengzihui_app.views.active_user,name='active_user'),

	#商家入住首页
	url(r'^busindex/$',zhengzihui_app.views.busindex,name='busindex'),
	url(r'^buspubservice/',zhengzihui_app.views.buspubservice,name='buspubservice'),
	url(r'^busmaservice/',zhengzihui_app.views.busmaservice,name='busmaservice'),
	url(r'^merge_service_details/',zhengzihui_app.views.merge_service_details,name='merge_service_details'),

]


