#coding:utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite #import for Adminsite change the header and title


from .models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News,Tb_Notice,Tb_Notice_Class,Tb_Apage,Tb_Apage_Class#引入需要管理的表单
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


admin.site.register(tb_user_expand)
admin.site.register(tb_user)
admin.site.register(tb_service_provider)
admin.site.register(tb_News_Class)
admin.site.register(tb_News)

admin.site.register(Tb_Notice,Tb_NoticeAdmin)
admin.site.register(Tb_Notice_Class,Tb_Notice_ClassAdmin)
admin.site.register(Tb_Apage,Tb_ApageAdmin)
admin.site.register(Tb_Apage_Class,Tb_Apage_ClassAdmin)
