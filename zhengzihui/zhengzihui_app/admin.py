#coding:utf-8
from django.contrib import admin
from django.contrib.admin import AdminSite #import for Adminsite change the header and title


from .models import tb_user_expand,tb_user,tb_service_provider,tb_News_Class,tb_News #引入需要管理的表单
# Register your models here.



admin.site.register(tb_user_expand)
admin.site.register(tb_user)
admin.site.register(tb_service_provider)
admin.site.register(tb_News_Class)
admin.site.register(tb_News)
