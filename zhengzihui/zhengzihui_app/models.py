#coding:utf-8
import datetime

from django.db import models
from django.utils import timezone#引入datetime 和 timezone 为了was_published_recently函数

from filer.fields.image import FilerImageField #YZ add for filer
from filer.fields.file import FilerFileField

# Create your models here.

    

class tb_user(models.Model):
    user_id = models.AutoField("用户id",primary_key = True)
    user_name = models.CharField("用户名称",max_length=100,null=False,blank=False)
    user_password = models.CharField("密码",max_length=100,null=False,blank=False)
    user_telephone = models.CharField("电话",max_length=40,null=False,blank=False)
    user_email = models.EmailField("用户邮箱",null=False,blank=False)
    
    PASSAUTH = 1
    NOTPASSAUTH = 0
    USER_AUTH_CHOICES = (
    (PASSAUTH,'通过验证'),
    (NOTPASSAUTH,"验证没有通过或者没有验证"),
    
    )
    user_auth = models.CharField("用户验证状态",max_length=20,choices=USER_AUTH_CHOICES,default=NOTPASSAUTH)#用户验证状态0：验证没有通过或者没有验证1：验证通过
    
    
    Enterprise = 1
    Personal = 0
    User_Type_CHOICES = (
    (Personal,'个人用户'),
    (Enterprise,'企业用户'),
    )
    user_type = models.CharField("注册用户类型",max_length=20,choices=User_Type_CHOICES,default=Personal)


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
    user_id = models.AutoField("用户id",primary_key=True)
    company_tel = models.CharField("办公电话",max_length=30,null=False,blank=False)
    company_email = models.EmailField("办公邮箱",null=False,blank=False)
    company_name = models.CharField("公司名称",max_length=30,null=False,blank=False)
    company_district = models.CharField("公司所在区县",max_length=50,null=False,blank=False)
    company_address = models.CharField("公司注册地址",max_length=50,null=False,blank=False)
    company_registered_capital = models.IntegerField("公司注册资本",null=False,blank=False)
    company_industry = models.CharField("公司所属行业",max_length=30,null=False,blank=False)
    company_stuff_no = models.IntegerField("公司人数",null=False,blank=False)
    company_nature = models.CharField("公司性质",max_length=30,null=False,blank=False)

    def __str__(self):
        return self.company_name

    def __str__(self):
        return self.company_email

    def __str__(self):
        return self.company_tel


class  tb_service_provider(models.Model):
    sp_code = models.IntegerField("服务提供商编码",primary_key=True,null=False,blank=False)
    sp_id = models.IntegerField("内部ID",null=False,blank=False)
    sp_name = models.CharField("服务商名称",max_length=40,null=False,blank=False)
    psw = models.CharField("密码",max_length=40,null=False,blank=False)

    tel = models.CharField("电话",max_length=40,null=False,blank=False)
    email = models.EmailField("邮箱",null=False,blank=False)
    master = models.CharField("擅长领域",max_length=50,null=False,blank=False)
    sp_image1 = models.ImageField("政资汇账户所有人身份证证件上传",null=False,blank=False)
    sp_image2 = models.ImageField("账户所代表的公司执照上传",null=False,blank=False)
    sp_grade = models.IntegerField("服务商等级",null=False,blank=False)
    sp_sort = models.IntegerField("排序",null=False,blank=False)
    area_id = models.CharField("服务提供商所在地",max_length=10,null=False,blank=False)
    Register_cap = models.IntegerField("注册资金",null=False,blank=False)
    staff_number = models.IntegerField("职员人数",null=False,blank=False)
    Annual_totals = models.IntegerField("年营业额",null=False,blank=False)
    organization_name = models.CharField("机构名称",max_length=40,null=False,blank=False)
    organization_id = models.IntegerField("机构代码",null=False,blank=False)
    organization_assets = models.IntegerField("机构资产",null=False,blank=False)
    organization_profile = models.CharField("机构简介",max_length=100,null=False,blank=False)
    
        
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
    
    sp_auth = models.CharField("服务商认证状态",max_length=20,choices=SP_AUTH_CHOICES,default=NOTPASSAUTH,null=False,blank=False)
    
    RECOMMEND = 1
    NOTRECOMMED = 0
    IS_RECOMMEND_CHOICES = (
    (RECOMMEND,'优先推荐(当有相同报价的服务商，是否优先考虑推荐)'),
    (NOTRECOMMED,'不优先推荐'),
    )
    is_recommend = models.CharField("是否优先推荐",max_length=20,choices=IS_RECOMMEND_CHOICES,default=RECOMMEND,null=False,blank=False)
    
    
class tb_News_Class(models.Model):
    necl_id = models.AutoField("分类id",primary_key=True)
    necl_code = models.IntegerField("分类标识码",null=False,blank=False)
    necl_name = models.CharField("分类名称",max_length=100,null=False,blank=False)
    necl_parent_id = models.IntegerField("父类ID",null=False,blank=False)#估计是之后需要添加的外键
    necl_sort = models.IntegerField("排序",null=False,blank=False)

    def __str__(self):
        return self.necl_name


class tb_News(models.Model):
    news_id = models.AutoField("新闻id",primary_key=True)
    article_id = models.IntegerField("文章ID",null=False,blank=False)
    news_time = models.DateTimeField("发布时间",null=False,blank=False)
    news_source = models.CharField("新闻来源",max_length=100,null=False,blank=False)
    necl_id = models.IntegerField("分类ID",null=False,blank=False)#之后需要添加的外键
    news_sort = models.IntegerField("新闻排序",null=False,blank=False)
    click_counter = models.IntegerField("总点击量",null=False,blank=False)
    
    HASALBUM = 1
    NOTHASALBUM = 0
    HAS_ALBUM_CHOICES = (
    (HASALBUM,'拥有相册'),
    (NOTHASALBUM,'没有相册'),
    )
    
    has_album =  models.CharField("是否拥有自己的相册",max_length=20,choices=HAS_ALBUM_CHOICES,default=NOTHASALBUM,null=False,blank=False)
    
    HOT = 1
    NOTHOT = 0
    NEWS_HOT_CHOICES=(
    (HOT,'热点新闻'),
    (NOTHOT,'非热点新闻'),
    
    )
    news_hot = models.CharField("是否为热点新闻",max_length=20,choices=NEWS_HOT_CHOICES,default=NOTHOT,null=False,blank=False)
    
    TOP = 1
    NOTTOP = 0
    NEWS_TOP_CHOICES=(
    (TOP,'置顶新闻'),
    (NOTTOP,'非置顶新闻'),
    
    )
    new_top = models.CharField("是否为置顶新闻",max_length=20,choices=NEWS_TOP_CHOICES,default=NOTTOP,null=False,blank=False)
    
    DISPLAY = 1
    NOTDISPLAY = 0
    NEWS_IS_DISPLAY_CHOICES=(
    (DISPLAY,'前端展示新闻'),
    (NOTDISPLAY,'非前端展示新闻'),
    
    )
    new_is_display =  models.CharField("是否为前端展示新闻",max_length=20,choices=NEWS_IS_DISPLAY_CHOICES,default=NOTDISPLAY,null=False,blank=False)
    

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
    
    
class tb_item(models.Model):
    item_id = models.IntegerField('ID', primary_key=True, null=False)
    item_code = models.CharField(max_length=20,null=False)
    item_name = models.CharField(max_length=100,null=False)
    itcl_id = models.IntegerField(null=False)
    item_level = models.IntegerField(null=False)
    item_ga = models.CharField(max_length=40,null=False)
    item_pa_id = models.IntegerField(null=False)
    item_publish = models.IntegerField(null=False)
    item_deadtime = models.IntegerField(null=False)
    item_about = models.CharField(max_length=100,null=False)
    item_url = models.CharField(max_length=100,null=False)
    item_key = models.TextField(null=False)
    item_status = models.IntegerField(null=False)
    is_hot = models.IntegerField(null=False)
    item_from = models.IntegerField(null=False,default = 0)
    is_recommend = models.IntegerField(null=False,default = 0)
    def __str__(self):
        return self.item_name

class tb_item_class(models.Model):
    itcl_id = models.IntegerField('ID', primary_key=True,null=False)
    itcl_code = models.IntegerField(null=False)
    itcl_name = models.CharField(max_length=100,null=False)
    itcl_des = models.CharField(max_length=100,null=False)
    necl_parent_id = models.IntegerField(null=False)
    necl_sort = models.IntegerField(null=False)


class tb_item_pa(models.Model):
    ipa_id = models.IntegerField('ID', primary_key=True,null=False)
    ipa_name = models.CharField(max_length=100,null=False)
    ipa_parent_id = models.IntegerField(null=False)
    ipa_sort = models.IntegerField(null=False)
    area_id = models.IntegerField(null=False)
    def __str__(self):
        return self.ipa_name
  


class tb_article(models.Model):
    article_id = models.IntegerField('ID', primary_key=True,null=False)
    article_code = models.IntegerField(null=False)
    article_name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    author_email = models.CharField(max_length=100,null=False)
    article_type = models.IntegerField(null=False)
    affiliation_id = models.IntegerField(null=False)
    article_content = models.TextField(null=False)
    article_keywords = models.TextField(null=False)
    article_des = models.CharField(max_length=100,null=False)
    article_sort = models.IntegerField(null=False)
    upload_time = models.DateTimeField(max_length=100,auto_now =True,null = False)
    is_default = models.IntegerField(null=False)
    article_click = models.IntegerField(null=False)

class tb_album(models.Model):
    album_id = models.AutoField('ID', primary_key=True,null=False)
    album_name = models.CharField(max_length=40,null=False)
    album_type = models.IntegerField(null=False)
    affiliation_id = models.IntegerField(null=False)
    nacl_des = models.CharField(max_length=100,null=False)
    nacl_sort = models.IntegerField(null=False)
    nacl_cover = models.CharField(max_length=100,null=False)
    upload_time = models.DateTimeField(max_length=100,auto_now = True,null = False)
    is_default = models.IntegerField(null=False)



class tb_pic(models.Model):
    pic_id = models.IntegerField('ID', primary_key=True,null=False)
    pic_name = models.CharField(max_length=40,null=False)
    pic_tag = models.CharField(max_length=40,null=False)
    album_id = models.IntegerField(null=False)
    pic_uri = models.CharField(max_length=100,null=False)   
    pic_size = models.IntegerField(null=False)
    pic_spec = models.CharField(max_length=100,null=False)
    upload_time = models.DateTimeField(max_length=100,auto_now = True,null = False)
    is_thumb = models.IntegerField(null=False)

    



class tb_accessory(models.Model):
    anne_id=models.IntegerField(null = False)
    comm_id=models.IntegerField(null = False)
    apubdate=models.IntegerField(null = False)
    apublisher = models.CharField(max_length=2,null =False)
    aposition= models.CharField(max_length=10,null =False)
    aaddtion= models.CharField(max_length=50)



class tb_Artificial_Representations(models.Model):
	arre_id = models.AutoField(primary_key = True)
	arre_title = models.CharField(max_length = 100, null = False)#申诉标题
	arre_content = models.TextField(max_length = 1000, null = False)#申诉内容
	user_id = models.IntegerField(null = False)#申诉人id
	user_name = models.CharField(max_length = 100, null = False)#申诉人名称
	arre_state = models.IntegerField(null = False)#申述状态0：未受理	1：已受理	2：已解决
	create_time = models.DateTimeField('提交申请时间')
	


class tb_Message(models.Model):
	mess_id = models.IntegerField(primary_key = True)
	send_id = models.IntegerField(null = False)#发送方ID
	rec_id = models.IntegerField(null = False)#接受方ID
	text_id = models.IntegerField(null = False)#文本ID
	status = models.IntegerField(null = False)#消息状态
    
class tb_MessageText(models.Model):
	text_id = models.IntegerField(primary_key = True)
	mete_title = models.CharField(max_length = 10, null = False)#短信标题
	mete_content = models.CharField(max_length = 300, null = False)#短信内容
	mete_time = models.DateTimeField('消息发送时间')
	    
class tb_SysMessage(models.Model):
	sys_id = models.IntegerField(primary_key = True)
	cust_id = models.IntegerField(null = False)#客户ID
	mess_id = models.IntegerField(null = False)#短信ID
	sys_status = models.IntegerField(null = False)#消息状态，0/1：已读/未读    
        
    
class tb_goods(models.Model):
    goods_id = models.IntegerField(primary_key = True)#自增索引id主键
    item_id = models.IntegerField(null = False)#服务对应项目的id
    sp_id = models.IntegerField(null = False)#服务对应的服务提供商
    goods_name = models.CharField(max_length = 40, null = False)#服务名称
    goods_show = models.IntegerField(null = False)#是否显示，0为否，1为是，默认为1
    goods_market_price = models.IntegerField(null = False)#服务市场报价
    goods_price = models.IntegerField(null = False)#服务未打折扣报价(标价)
    goods_price_discouint = models.FloatField(null = False)#折扣（标价乘以折扣等于实际成交价）
    goods_pay = models.IntegerField(null = False)#该服务支持的支付方式
    goods_guarantee = models.CharField(max_length = 100, null = False)#商家保证
    goods_status = models.IntegerField(null = False)#服务提供商服务状态：0不可服务1可服务2暂时不可服务
    goods_sort = models.IntegerField(null = False)#排序
    goods_commend = models.IntegerField(null = False)#是否推荐此服务交易
    goods_evaluation_good_star = models.IntegerField(null = False)#好评星级
    goods_evaluation_count = models.IntegerField(null = False)#评价数
    goods_successrate = models.IntegerField(null=False,default=50)#成功率
    
    
    
    
    
    
