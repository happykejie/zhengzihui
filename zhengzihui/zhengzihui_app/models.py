﻿#coding:utf-8
import datetime

from django.db import models
from django.utils import timezone#引入datetime 和 timezone 为了was_published_recently函数

from filer.fields.image import FilerImageField #YZ add for filer
from filer.fields.file import FilerFileField

# Create your models here.
#所有数据库字段的开头字母大写，所有表单的id前需要加上表单名
defaultURL = 'default'
defaultImageURLofNews = 'img/News_img/%Y/%m/%d' #每次makemigration的时候好像是需要在not null 字段加入default
defaultImageURLofAds = 'img/Ads_img/%Y/%m/%d'
defaultImageURLofProduct = 'img/Product_img/%Y/%m/%d'

defaultFileURLofProduct = 'file/Product_file/%Y/%m/%d'

class News(models.Model):
    News_id = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 1000,null = False)
    Content = models.TextField(max_length = 10000,null = False)
    Image = models.ImageField(upload_to = defaultImageURLofNews,default = 'img/News_img/None/no-img.jpg')
    Publish_Date = models.DateTimeField('date published')    
    Publish_Editer = models.CharField(max_length=100,null = False)
    
    def __str__(self):              # 在此处有__str__函数的字段能够在admin中显示其值
        return self.Title
    def __str__(self):              # __unicode__ on Python 2
        return self.Content
    
    def was_published_recently(self):
        return self.Publish_Date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Product(models.Model):
    Product_id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=100,null = False)
    Image = models.ImageField(upload_to = defaultImageURLofProduct,default = 'img/Product_img/None/no-img.jpg')
    Info = models.TextField(max_length=10000,null = False)
    FileAbout = models.FileField(upload_to=defaultFileURLofProduct,default =defaultURL)
    Price = models.IntegerField(null = False)
    Puton_Stuff = models.CharField(max_length=100,null = False)
    
    def __str__(self):
        return self.Name
    def __str__(self):
        return self.Info

    
        
class Ads(models.Model):
    Ads_id = models.AutoField(primary_key = True)
    Title = models.CharField(max_length=100,null =False)
    Image = models.ImageField(upload_to = defaultImageURLofAds,default = 'img/Ads_img/None/no-img.jpg')
    Content = models.TextField(max_length=1000,null =False)
    
    Puton_Stuff = models.CharField(max_length=100,null = False)
    
class Tb_Notice(models.Model):
    Notice_id = models.AutoField(primary_key = True)  
    Notice_title = models.CharField('公告标题',max_length=100,null =False)
    Article_id = models.IntegerField('文章ID',null =False)
    Notice_time = models.DateField('发布时间')
    Notice_source = models.CharField('公告来源',max_length=100,null =False)
    Nocl_id = models.IntegerField('分类ID',null =False)
    Notice_sort = models.IntegerField('排序',null =False)
    Notice_is_display= models.IntegerField('是否显示',null =False)
    Notice_top = models.IntegerField('强制置顶',null =False)
	
    def __str__(self):
        return self.Notice_title
    def __str__(self):
        return self.Notice_source


class Tb_Notice_Class(models.Model):
    Nocl_id = models.IntegerField('分类ID',null =False,primary_key = True)
    Nocl_code = models.IntegerField('分类标识码',null =False)
    Nocl_name = models.CharField('分类名称',max_length=100,null =False)
    Nocl_des = models.CharField('分类描述',max_length=100,null =False)
    Nocl_parent_id = models.IntegerField('父类ID')
    Notice_sort = models.IntegerField('排序',null =False)
	
    def __str__(self):
        return self.Nocl_name
    def __str__(self):
        return self.Nocl_des


class Tb_Apage(models.Model):
     Apage_id = models.AutoField('单页ID',null =False,primary_key = True)
     Article_id = models.IntegerField('文章ID',null =False)
     Has_album = models.IntegerField('是否含有相册',null =False)
     Apage_time = models.DateField('发布时间')
     Apage_source = models.CharField('单页来源',max_length=100)
     Apcl_id = models.IntegerField('分类ID',null =False)
     Apage_sort = models.IntegerField('排序',null =False)
     Apage_is_display = models.IntegerField('是否显示',null =False)
     def __str__(self):
        return self.Apage_source
    
class Tb_Apage_Class(models.Model):
     Apcl_id = models.IntegerField('单页分类ID',null =False,primary_key = True)
     Apcl_code = models.IntegerField('分类标识码',null =False)
     Apcl_name = models.CharField('分类名称',max_length=100,null =False)
     Apcl_parent_id = models.IntegerField('父类ID')
     Apcl_sort = models.IntegerField('排序',null =False)
     def __str__(self):
        return self.Apcl_name
    
    
    
 

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover = FilerImageField(null=True, blank=True,related_name="book_covers")
    back = FilerImageField(null=True, blank=True,related_name="book_backs")
    content = FilerFileField(null=True, blank=True,related_name="company_disclaimer")
    
    
    
    
    
    
    
    
    
    
    
    
    
