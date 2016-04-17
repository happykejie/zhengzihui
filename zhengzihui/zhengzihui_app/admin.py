﻿#coding:utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite #import for Adminsite change the header and title


from .models import Ads,News,Product,Book,tb_article,tb_album,tb_pic,tb_accessory #引入需要管理的表单
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
    
admin.site.register(Ads,AdsAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Book)
admin.site.register(tb_article)
admin.site.register(tb_album)
admin.site.register(tb_pic)
admin.site.register(tb_accessory)
