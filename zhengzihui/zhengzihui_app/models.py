#coding:utf-8
import datetime

from django.db import models
from django.utils import timezone#引入datetime 和 timezone 为了was_published_recently函数

from filer.fields.image import FilerImageField #YZ add for filer
from filer.fields.file import FilerFileField

# Create your models here.

    

class tb_user(models.Model):
    user_id = models.AutoField(primary_key = True,help_text="用户id")
    user_name = models.CharField(max_length=100,null=False,blank=False,help_text="用户名称")
    user_password = models.CharField(max_length=100,null=False,blank=False,help_text="密码")
    user_telephone = models.CharField(max_length=40,null=False,blank=False,help_text="电话")
    user_email = models.EmailField(null=False,blank=False,help_text="用户邮箱")
	
    PASSAUTH = 1
    NOTPASSAUTH = 0
    USER_AUTH_CHOICES = (
    (PASSAUTH,'通过验证'),
    (NOTPASSAUTH,"验证没有通过或者没有验证"),
    
    )
    user_auth = models.CharField(max_length=20,choices=USER_AUTH_CHOICES,default=NOTPASSAUTH,help_text="用户验证状态")#用户验证状态0：验证没有通过或者没有验证1：验证通过
    
    
    Enterprise = 1
    Personal = 0
    User_Type_CHOICES = (
    (Personal,'个人用户'),
    (Enterprise,'企业用户'),
    )
    user_type = models.CharField(max_length=20,choices=User_Type_CHOICES,default=Personal,help_text="注册用户类型")


    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.user_email

    def __str__(self):
        return self.user_telephone

    def __str__(self):
        return self.user_auth

    def __str__(self):
        return self.user_type

class tb_user_expand(models.Model):
    user_id = models.AutoField(primary_key=True,help_text="用户id")
    company_tel = models.CharField(max_length=30,null=False,blank=False,help_text="办公电话")
    company_email = models.EmailField(null=False,blank=False,help_text="办公邮箱")
    company_name = models.CharField(max_length=30,null=False,blank=False,help_text="公司名称")
    company_district = models.CharField(max_length=50,null=False,blank=False,help_text="公司所在区县")
    company_address = models.CharField(max_length=50,null=False,blank=False,help_text="公司注册地址")
    company_registered_capital = models.IntegerField(null=False,blank=False,help_text="公司注册资本")
    company_industry = models.CharField(max_length=30,null=False,blank=False,help_text="公司所属行业")
    company_stuff_no = models.IntegerField(null=False,blank=False,help_text="公司人数")
    company_nature = models.CharField(max_length=30,null=False,blank=False,help_text="公司性质")

    def __str__(self):
        return self.company_name

    def __str__(self):
        return self.company_email

    def __str__(self):
        return self.company_tel


class  tb_service_provider(models.Model):
    sp_code = models.IntegerField(primary_key=True,null=False,blank=False,help_text="服务提供商编码")
    sp_id = models.IntegerField(null=False,blank=False,help_text="内部ID")
    sp_name = models.CharField(max_length=40,null=False,blank=False,help_text="服务商名称")
    psw = models.CharField(max_length=40,null=False,blank=False,help_text="密码")

    tel = models.CharField(max_length=40,null=False,blank=False,help_text="电话")
    email = models.EmailField(null=False,blank=False,help_text="邮箱")
    master = models.CharField(max_length=50,null=False,blank=False,help_text="擅长领域")
    sp_image1 = models.ImageField(null=False,blank=False,help_text="政资汇账户所有人身份证证件上传")
    sp_image2 = models.ImageField(null=False,blank=False,help_text="账户所代表的公司执照上传")
    sp_grade = models.IntegerField(null=False,blank=False,help_text="服务商等级")
    sp_sort = models.IntegerField(null=False,blank=False,help_text="排序")
    area_id = models.CharField(max_length=10,null=False,blank=False,help_text="服务提供商所在地")
    Register_cap = models.IntegerField(null=False,blank=False,help_text="注册资金")
    staff_number = models.IntegerField(null=False,blank=False,help_text="职员人数")
    Annual_totals = models.IntegerField(null=False,blank=False,help_text="年营业额")
    organization_name = models.CharField(max_length=40,null=False,blank=False,help_text="机构名称")
    organization_id = models.IntegerField(null=False,blank=False,help_text="机构代码")
    organization_assets = models.IntegerField(null=False,blank=False,help_text="机构资产")
    organization_profile = models.CharField(max_length=100,null=False,blank=False,help_text="机构简介")
    
        
    PASSAUTH = 1
    NOTPASSAUTH = 0
    WAITAUTH = 2
    AUTHING = 3
    SP_AUTH_CHOICES=(
    (NOTPASSAUTH,"未通过认证"),
    (PASSAUTH,"通过认证"),
    (WAITAUTH,"等待被认证"),
    (AUTHING,"正在认证"),
    )
    
    sp_auth = models.CharField(max_length=20,choices=SP_AUTH_CHOICES,default=NOTPASSAUTH,null=False,blank=False,help_text="服务商认证状态")
    
    RECOMMEND = 1
    NOTRECOMMED = 0
    IS_RECOMMEND_CHOICES = (
    (RECOMMEND,'优先推荐(当有相同报价的服务商，是否优先考虑推荐)'),
    (NOTRECOMMED,'不优先推荐'),
    )
    is_recommend = models.CharField(max_length=20,choices=IS_RECOMMEND_CHOICES,default=RECOMMEND,null=False,blank=False,help_text="是否优先推荐")
    
    
class tb_News_Class(models.Model):
    necl_id = models.AutoField(primary_key=True,help_text="分类id")
    necl_code = models.IntegerField(null=False,blank=False,help_text="分类标识码")
    necl_name = models.CharField(max_length=100,null=False,blank=False,help_text="分类名称")
    necl_parent_id = models.IntegerField(help_text="父类ID")#估计是之后需要添加的外键
    necl_sort = models.IntegerField(help_text="排序")

    def __str__(self):
        return self.necl_name


class tb_News(models.Model):
    news_id = models.AutoField(primary_key=True,help_text="新闻id")
    article_id = models.IntegerField(null=False,blank=False,help_text="文章ID")
    news_time = models.DateTimeField(null=False,blank=False,help_text="发布时间")
    news_source = models.CharField(max_length=100,null=False,blank=False,help_text="新闻来源")
    necl_id = models.IntegerField(null=False,blank=False,help_text="分类ID")#之后需要添加的外键
    news_sort = models.IntegerField(null=False,blank=False,help_text="新闻排序")
    click_counter = models.IntegerField(null=False,blank=False,help_text="总点击量")
    
    HASALBUM = 1
    NOTHASALBUM = 0
    HAS_ALBUM_CHOICES = (
    (HASALBUM,'拥有相册'),
    (NOTHASALBUM,'没有相册'),
    )
    
    has_album =  models.CharField(max_length=20,choices=HAS_ALBUM_CHOICES,default=NOTHASALBUM,null=False,blank=False,help_text="是否拥有自己的相册")
    
    HOT = 1
    NOTHOT = 0
    NEWS_HOT_CHOICES=(
    (HOT,'热点新闻'),
    (NOTHOT,'非热点新闻'),
    
    )
    news_hot = models.CharField(max_length=20,choices=NEWS_HOT_CHOICES,default=NOTHOT,null=False,blank=False,help_text="是否为热点新闻")
    
    TOP = 1
    NOTTOP = 0
    NEWS_TOP_CHOICES=(
    (TOP,'置顶新闻'),
    (NOTTOP,'非置顶新闻'),
    
    )
    new_top = models.CharField(max_length=20,choices=NEWS_TOP_CHOICES,default=NOTTOP,null=False,blank=False,help_text="是否为置顶新闻")
    
    DISPLAY = 1
    NOTDISPLAY = 0
    NEWS_IS_DISPLAY_CHOICES=(
    (DISPLAY,'前端展示新闻'),
    (NOTDISPLAY,'非前端展示新闻'),
    
    )
    new_is_display =  models.CharField(max_length=20,choices=NEWS_IS_DISPLAY_CHOICES,default=NOTDISPLAY,null=False,blank=False,help_text="是否为前端展示新闻")
	

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
    
    
    
    
    
    
    
    
    
    
    
    
