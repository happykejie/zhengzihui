﻿#coding:utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite #import for Adminsite change the header and title


from .models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class,tb_article,tb_album,tb_pic,tb_accessory,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage,tb_item_pa,tb_item_class,tb_goods,tb_item#引入需要管理的表单
# Register your models here.
class Tb_Apage_ClassAdmin(admin.ModelAdmin):
    fieldsets = [
            ('添加单页分类',{'fields':['Apcl_id','Apcl_code','Apcl_name','Apcl_parent_id']}),
            ('其他',{'fields':['Apcl_sort'],'classes': ['collapse']}),
    ]
    list_display = ['Apcl_id','Apcl_name','Apcl_parent_id']

class Tb_ApageAdmin(admin.ModelAdmin):
    fieldsets = [
            ('添加单页',{'fields':['Article_id','Apage_source']}),
            ('其他',{'fields':['Has_album','Apage_time','Apcl_id','Apage_sort','Apage_is_display'],'classes': ['collapse']}),
    ]
    list_display = ['Apage_id','Article_id','Apage_source','Apage_time']

class Tb_Notice_ClassAdmin(admin.ModelAdmin):
    fieldsets = [
            ('添加公告分类',{'fields':['Nocl_id','Nocl_code','Nocl_name']}),
            ('其他',{'fields':['Nocl_des','Nocl_parent_id','Notice_sort'],'classes': ['collapse']}),
    ]
    list_display = ['Nocl_id','Nocl_name','Nocl_des']
   # list_filter = ['Notice_time']
   # search_fields = ['Notice_title'] #如何进入description 以提示搜索标题

class Tb_NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
            ('添加公告标题内容和来源',{'fields':['Notice_title','Article_id','Notice_source']}),
            ('其他',{'fields':['Notice_time','Nocl_id','Notice_sort','Notice_is_display','Notice_top'],'classes': ['collapse']}),
    ]
    list_display = ['Notice_title','Notice_source','Notice_time']
   # list_filter = ['Notice_time']
   # search_fields = ['Notice_title'] #如何进入description 以提示搜索标题
   
   
class tb_Artificial_Representations_Admin(admin.ModelAdmin):
	fieldsets = [
            ('添加申诉信息',{'fields':['arre_title','arre_content','user_id','user_name','arre_state']}),
            ('添加日期',{'fields':['create_time'],'classes': ['collapse']}),
    
    ]
	list_display = ['arre_title', 'arre_content', 'user_id', 'user_name', 'arre_state', 'create_time']
	
	
class tb_Message_Admin(admin.ModelAdmin):
	fieldsets = [
            ('添加站内短信ID信息',{'fields':['mess_id','send_id','rec_id','text_id','status']}),
    
    ]
	list_display = ['mess_id', 'send_id', 'rec_id', 'text_id', 'status']
	
	
class tb_MessageText_Admin(admin.ModelAdmin):
	fieldsets = [
            ('添加短信内容信息',{'fields':['text_id','mete_title','mete_content']}),
            ('添加日期',{'fields':['mete_time'],'classes': ['collapse']}),
    
    ]
	list_display = ['text_id', 'mete_title', 'mete_content', 'mete_time']
	
	
class tb_SysMessage_Admin(admin.ModelAdmin):
	fieldsets = [
            ('添加站内系统短信信息',{'fields':['sys_id','cust_id','mess_id','sys_status']}),            
    
    ]
	list_display = ['sys_id', 'cust_id', 'mess_id', 'sys_status']


class tb_item_pa_Admin(admin.ModelAdmin):
    fieldsets = [
            ('添加项目发布机构',{'fields':['ipa_id','ipa_name','ipa_parent_id','ipa_sort','area_id']}),
    
    ]
    list_display = ['ipa_id', 'ipa_name', 'ipa_parent_id', 'ipa_sort', 'area_id']

class tb_item_Admin(admin.ModelAdmin):
    fieldsets = [
            ('添加项目',{'fields':['item_id','item_code','item_name','item_level','item_ga','item_pa_id','item_publish','item_deadtime','item_about','item_url','item_key','item_status','is_hot','item_from','is_recommend']}),
    
    ]
    list_display = ['item_id', 'item_code', 'item_name', 'item_level', 'item_ga','item_pa_id','item_publish','item_deadtime','item_about','item_url','item_key','item_status','is_hot','item_from','is_recommend']


class tb_item_class_Admin(admin.ModelAdmin):
    fieldsets = [
            ('添加项目分类',{'fields':['itcl_id','itcl_code','itcl_name','itcl_des','necl_parent_id','necl_sort']}),
    
    ]
    list_display = ['itcl_id', 'itcl_code', 'itcl_name', 'itcl_des', 'necl_parent_id','necl_sort']

admin.site.register(tb_user_expand)
admin.site.register(tb_user)
admin.site.register(tb_service_provider)
admin.site.register(tb_News_Class)
admin.site.register(tb_News)
admin.site.register(tb_goods)

admin.site.register(Tb_Notice,Tb_NoticeAdmin)
admin.site.register(Tb_Notice_Class,Tb_Notice_ClassAdmin)
admin.site.register(Tb_Apage,Tb_ApageAdmin)
admin.site.register(Tb_Apage_Class,Tb_Apage_ClassAdmin)


admin.site.register(tb_article)
admin.site.register(tb_album)
admin.site.register(tb_pic)
admin.site.register(tb_accessory)
admin.site.register(tb_item)

admin.site.register(tb_Artificial_Representations,tb_Artificial_Representations_Admin)
admin.site.register(tb_Message,tb_Message_Admin)
admin.site.register(tb_MessageText,tb_MessageText_Admin)
admin.site.register(tb_SysMessage,tb_SysMessage_Admin)


admin.site.register(tb_item_pa,tb_item_pa_Admin)
admin.site.register(tb_item_class,tb_item_class_Admin)
