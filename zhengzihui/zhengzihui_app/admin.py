#coding:utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite #import for Adminsite change the header and title


from .models import Ads,News,Product,Book,tb_Artificial_Representations,tb_Message,tb_MessageText,tb_SysMessage#引入需要管理的表单
# Register your models here.





class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
            ('添加文章标题和内容',{'fields':['Title','Content']}),
            ('添加发文日期和发文编辑',{'fields':['Publish_Date','Publish_Editer'],'classes': ['collapse']}),
    
    ]
    list_display = ['Title','Content','Publish_Date','was_published_recently']
    list_filter = ['Publish_Date']
    search_fields = ['Title'] #如何进入description 以提示搜索标题

class AdsAdmin(admin.ModelAdmin):
    list_display = ['Title','Content','preview']

    def preview(self,obj):

        return '<img src="/static/zhengzihui_app/%s" height="256" width="256" />' %(obj.Image)

    preview.allow_tags = True
    preview.short_description = "Ads Picture"
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name','Price','Info','FileAbout','preview']
    
    def preview(self,obj):

        return '<img src="/static/zhengzihui_app/%s" height="64" width="64" />' %(obj.Image)

    preview.allow_tags = True
    preview.short_description = "Product Picture"
    
	
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

admin.site.register(Ads,AdsAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Book)
admin.site.register(tb_Artificial_Representations,tb_Artificial_Representations_Admin)
admin.site.register(tb_Message,tb_Message_Admin)
admin.site.register(tb_MessageText,tb_MessageText_Admin)
admin.site.register(tb_SysMessage,tb_SysMessage_Admin)


