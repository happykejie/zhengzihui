#coding:utf-8
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
    
    
    
    
    
    
    
    
    
    
 

class Book(models.Model):
    title = models.CharField(max_length=255)
    cover = FilerImageField(null=True, blank=True,related_name="book_covers")
    back = FilerImageField(null=True, blank=True,related_name="book_backs")
    content = FilerFileField(null=True, blank=True,related_name="company_disclaimer")
    
    
    
    
    
    
    
    
    
    
    
    
    
