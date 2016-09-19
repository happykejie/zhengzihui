#coding:utf-8
import datetime,time

from django.db import models
from django.utils import timezone#引入datetime 和 timezone 为了was_published_recently函数

from filer.fields.image import FilerImageField #YZ add for filer
from filer.fields.file import FilerFileField

# Create your models here.

#公共虚类

class Common_Area_Info(models.Model):
    # ...
    privince = models.CharField("省",max_length=100,null=True)
    city = models.CharField("市", max_length=100, null=True)
    distr = models.CharField("区", max_length=100, null=True)
    xianfen = models.CharField("县份", max_length=100, null=True)


    class Meta:
        abstract = True


class tb_user_expand(models.Model):
    user_id = models.AutoField("用户id",primary_key=True)
    company_tel = models.CharField("联系人移动电话",max_length=30,blank=False,null=True)
    company_email = models.EmailField("联系人邮箱",blank=False,null=True)
    company_name = models.CharField("公司名称",max_length=30,blank=False,null=True)
    company_district = models.CharField("公司所在区县",max_length=50,blank=False,null=True)
    company_address = models.CharField("公司注册地址",max_length=50,blank=False,null=True)
    company_registered_capital = models.IntegerField("公司注册资本",blank=False,null=True)
    company_industry = models.CharField("公司所属行业",max_length=30,blank=False,null=True)
    company_stuff_no = models.CharField("公司人数",max_length=30, blank=False,null=True)
    company_nature = models.CharField("公司性质",max_length=30,blank=False,null=True)
    companyUserContactName = models.CharField("联系人姓名", max_length=40, blank=False,null=True)
    companyUserPhone = models.CharField("固话", max_length=40, blank=False,null=True)  # 固话
    class Meta:
        verbose_name = '用户扩展信息'
        verbose_name_plural = '用户扩展信息'
    def __unicode__(self):
        return self.company_name

    def __unicode__(self):
        return self.company_email

    def __unicode__(self):
        return self.company_tel

    

class tb_user(models.Model):
    user_id = models.AutoField("用户id",primary_key = True)
    expand = models.ForeignKey(tb_user_expand,verbose_name='对应的扩展表',null=True)
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
    user_auth = models.IntegerField("用户验证状态",choices=USER_AUTH_CHOICES,default=NOTPASSAUTH)#用户验证状态0：验证没有通过或者没有验证1：验证通过
    
    
    Enterprise = 1
    Personal = 0
    User_Type_CHOICES = (
    (Personal,'个人用户'),
    (Enterprise,'企业用户'),
    )
    user_type = models.IntegerField("注册用户类型",choices=User_Type_CHOICES,default=Personal)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户' 

    def __unicode__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_email

    def __unicode__(self):
        return self.user_telephone
'''
    def __str__(self):
        return self.user_auth

    def __str__(self):
        return self.user_type
'''


'''
class tb_companyuser(models.Model):
    companyUserId = models.AutoField("用户id",primary_key = True)
    companyUserName = models.CharField("用户名",max_length=100,null=False,blank=False)
    companyUserPassword = models.CharField("密码",max_length=100,null=False,blank=False)
    companyUserCompanyName = models.CharField("公司名称",max_length=100,null=False,blank=False)
    companyUserCompanyLocation = models.CharField("公司位置",max_length=100,null=False,blank=False)#省市县
    companyUserCompanyAddress = models.CharField("公司地址",max_length=100,null=False,blank=False)
    companyUserCompanyCapital = models.CharField("注册资本",max_length=100,null=False,blank=False)
    companyUserCompanyPeople = models.CharField("公司人数",max_length=100,null=False,blank=False)
    companyUserCompanyIndustry = models.CharField("公司行业",max_length=100,null=False,blank=False)
    companyUserCompanyNature = models.CharField("公司性质",max_length=100,null=False,blank=False)
    companyUserContactName = models.CharField("联系人姓名",max_length=40,null=False,blank=False)
    companyUserPhone = models.CharField("固话", max_length=40, null=False, blank=False)#固话
    companyUserTelephone = models.CharField("手机", max_length=40, null=False, blank=False)#手机
    companyUserEmail = models.EmailField("用户邮箱", null=False, blank=False)

    def __unicode__(self):
        return self.companyUserName
    def __unicode__(self):
        return self.companyUserCompanyName
    def __unicode__(self):
        return self.companyUserContactName
'''




defaultImageURLoftb_service_provider_sp_image1 = 'img/tb_service_provider_sp_img1/%Y/%m/%d'
defaultImageURLoftb_service_provider_sp_image2 = 'img/tb_service_provider_sp_img2/%Y/%m/%d'
        
class  tb_service_provider(models.Model):
    #sp_code = models.IntegerField("服务提供商编码",primary_key=True,null=False,blank=False)
    sp_code = models.IntegerField("服务提供商编码",null=True,blank=False)
    #sp_id = models.IntegerField("内部ID",null=False,blank=False)
    sp_id = models.AutoField("内部ID",primary_key = True)
    sp_name = models.CharField("服务商名称",max_length=40,null=False,blank=False)
    psw = models.CharField("密码",max_length=40,null=True,blank=False)

    tel = models.CharField("电话",max_length=40,null=False,blank=False)
    email = models.EmailField("邮箱",null=False,blank=False)
    master = models.CharField("擅长领域",max_length=50,null=True,blank=False)
    sp_image1 = models.ImageField("政资汇账户所有人身份证证件上传",upload_to=defaultImageURLoftb_service_provider_sp_image1,null=True,blank=False)
    sp_image2 = models.ImageField("账户所代表的公司执照上传",upload_to=defaultImageURLoftb_service_provider_sp_image2,null=True,blank=False)
    sp_grade = models.IntegerField("服务商等级",null=True,blank=False)
    sp_sort = models.IntegerField("排序",null=True,blank=False)
    area_id = models.CharField("服务提供商所在地",max_length=10,null=True,blank=False)
    Register_cap = models.IntegerField("注册资金",null=True,blank=False)
    staff_number = models.IntegerField("职员人数",null=True,blank=False)
    Annual_totals = models.IntegerField("年营业额",null=True,blank=False)
    organization_name = models.CharField("机构名称",max_length=40,null=True,blank=False)
    organization_id = models.IntegerField("机构代码",null=True,blank=False)
    organization_assets = models.IntegerField("机构资产",null=True,blank=False)
    organization_profile = models.CharField("机构简介",max_length=100,null=True,blank=False)
    is_recommend = models.IntegerField('推荐指数',null=True)

    sp_type=models.CharField('合作类型',max_length=60,null=False,blank=False)
    con_name=models.CharField('联系人姓名',max_length=30,null=False,blank=False)
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
    
    sp_auth = models.IntegerField("服务商认证状态",choices=SP_AUTH_CHOICES,default=NOTPASSAUTH,null=False,blank=False)
    
    RECOMMEND = 1
    NOTRECOMMED = 0
    IS_RECOMMEND_CHOICES = (
    (RECOMMEND,'优先推荐(当有相同报价的服务商，是否优先考虑推荐)'),
    (NOTRECOMMED,'不优先推荐'),
    )
    is_recommend = models.IntegerField("是否优先推荐",choices=IS_RECOMMEND_CHOICES,default=RECOMMEND,null=False,blank=False)
    class Meta:
        verbose_name = '服务提供商'
        verbose_name_plural = '服务提供商' 
    def __str__(self):
        return self.sp_name

    def __str__(self):
        return str(self.sp_code)

   
    
class tb_News_Class(models.Model):
    necl_id = models.AutoField("分类id",primary_key=True)
    necl_code = models.IntegerField("分类标识码",null=False,blank=False)
    necl_name = models.CharField("分类名称",max_length=100,null=False,blank=False)
    necl_parent_id = models.IntegerField("父类ID",null=False,blank=False)#估计是之后需要添加的外键
    necl_sort = models.IntegerField("排序",null=False,blank=False)
    class Meta:
        verbose_name = '新闻类别'
        verbose_name_plural = '新闻类别' 
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
    news_hot = models.IntegerField('热门细纹',null=False)

    HASALBUM = 1
    NOTHASALBUM = 0
    HAS_ALBUM_CHOICES = (
    (HASALBUM,'拥有相册'),
    (NOTHASALBUM,'没有相册'),
    )
    
    has_album =  models.IntegerField("是否拥有自己的相册",choices=HAS_ALBUM_CHOICES,default=NOTHASALBUM,null=False,blank=False)
    
    HOT = 1
    NOTHOT = 0
    NEWS_HOT_CHOICES=(
    (HOT,'热点新闻'),
    (NOTHOT,'非热点新闻'),
    
    )
    news_hot = models.IntegerField("是否为热点新闻",choices=NEWS_HOT_CHOICES,default=NOTHOT,null=False,blank=False)
    
    TOP = 1
    NOTTOP = 0
    NEWS_TOP_CHOICES=(
    (TOP,'置顶新闻'),
    (NOTTOP,'非置顶新闻'),
    
    )
    new_top = models.IntegerField("是否为置顶新闻",choices=NEWS_TOP_CHOICES,default=NOTTOP,null=False,blank=False)
    
    DISPLAY = 1
    NOTDISPLAY = 0
    NEWS_IS_DISPLAY_CHOICES=(
    (DISPLAY,'前端展示新闻'),
    (NOTDISPLAY,'非前端展示新闻'),
    
    )
    new_is_display =  models.IntegerField("是否为前端展示新闻",choices=NEWS_IS_DISPLAY_CHOICES,default=NOTDISPLAY,null=False,blank=False)
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻' 
    def __str__(self):
        return str(self.news_id)
    def __str__(self):
        return str(self.article_id)
    def __str__(self):
        return str(self.news_time)
        

    


class Tb_Notice(models.Model):
    Notice_id = models.AutoField(primary_key = True)  
    Notice_title = models.CharField('公告标题',max_length=100,null =False)
    Notice_short_content = models.CharField('公告短内容',max_length=1000,null=True)
    Article_id = models.IntegerField('文章ID',null =False)
    Notice_time = models.DateField('发布时间')
    Notice_source = models.CharField('公告来源',max_length=100,null =False)
    Nocl_id = models.IntegerField('分类ID',null =False)
    Notice_sort = models.IntegerField('排序',null =False)
    Notice_is_display= models.IntegerField('是否显示',null =False)
    Notice_top = models.IntegerField('强制置顶',null =False)
    class Meta:
        verbose_name = '公告 '
        verbose_name_plural = '公告'     
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
    class Meta:
        verbose_name = '公告类别'
        verbose_name_plural = '公告类别'     
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
     class Meta:
        verbose_name = '单页表'
        verbose_name_plural = '单页表' 
     def __str__(self):
        return self.Apage_source
    
class Tb_Apage_Class(models.Model):
     Apcl_id = models.IntegerField('单页分类ID',null =False,primary_key = True)
     Apcl_code = models.IntegerField('分类标识码',null =False)
     Apcl_name = models.CharField('分类名称',max_length=100,null =False)
     Apcl_parent_id = models.IntegerField('父类ID')
     Apcl_sort = models.IntegerField('排序',null =False)
     class Meta:
        verbose_name = '单页分类表'
        verbose_name_plural = '单页分类表' 
     def __str__(self):
        return self.Apcl_name
    
    
class tb_item(Common_Area_Info):
    item_id = models.IntegerField('项目ID', primary_key=True, null=False,unique=True)
    item_code = models.CharField('项目编号',max_length=20,null=False,blank=False)
    item_name = models.CharField('项目名称',max_length=100,null=False,)
    itcl_id = models.IntegerField('项目分类ID',null=False)
    
    XIANJI = 1
    SHIJI = 2
    SHENGJI = 3
    ZHONGYANG = 4
    CAPITAL_LEVEL = (
    (XIANJI,'县级资金'),
    (SHIJI,'市级资金'),
    (SHENGJI,'省级资金'),
    (ZHONGYANG,'中央资金'),
    )
    item_level = models.IntegerField('项目资金级别',choices=CAPITAL_LEVEL,default=XIANJI,null=False,blank=False)

    item_ga = models.CharField('支持额度',max_length=40,null=False)
    item_pa_id = models.IntegerField('发布项目的机构的id',null=False)
    item_publish = models.DateTimeField('项目发布时间',null=False)
    item_deadtime = models.DateTimeField('项目截止时间',null=False)
    item_about = models.CharField('此项目的支持行业或者领域',max_length=100,null=False)
    item_url = models.CharField('项目通知的原文链接',max_length=100,null=False)
    item_key = models.TextField('项目关键字',null=False)

    NORMAL = 0
    TIMEUP = 1
    TEXTERROR = 2
    ITEM_STATUS = (
    (NORMAL,'正常'),
    (TIMEUP,'项目申报时间截止'),
    (TEXTERROR,'内容有误'),
    )

    item_status = models.IntegerField('项目状态',choices=ITEM_STATUS,default=NORMAL,null=False,blank=False)

    NOTHOT = 0
    HOT = 1
    NEW = 2
    IS_HOT = (
    (NOTHOT,'普通'),
    (HOT,'热门'),
    (NEW,'新出'),
    )
    is_hot = models.IntegerField('是否热门',choices=IS_HOT,default=NOTHOT,null=False,blank=False)

    SYS = 0
    PUBLISH = 1
    ITEM_FROM = (
    (SYS,'本系统爬虫获取'),
    (PUBLISH,'从发布信息获取'),
    
    )
    item_from = models.IntegerField('项目信息来源',choices=ITEM_FROM,default=SYS,null=False,blank=False)

    RECOMMEND = 1
    NOTRECOMMED = 0
    IS_RECOMMEND = (
    (RECOMMEND,'推荐'),
    (NOTRECOMMED,'不推荐'),
    
    )
    is_recommend = models.IntegerField('是否推荐',choices=IS_RECOMMEND,default=NOTRECOMMED,null=False,blank=False)
    class Meta:
        verbose_name = '项目详情表'
        verbose_name_plural = '项目详情表' 
    def __str__(self):   #python 2
        return self.item_name
    def get_remain_time(self):
        remain_time = '0'
        #time.time()是一个时间戳，相对一某个国际固定时间
        #将datatime类型转化了时间戳类型，用time.mktime(self.item_deadtime.timetuple())即可
        if (time.time() - time.mktime(self.item_deadtime.timetuple()))>0:
            return remain_time
        else:
            remain_time = str((time.mktime(self.item_deadtime.timetuple()) - time.time() ))
            #为什么不用int类型呢？好像是因为不能返回，暂时不清楚
            return remain_time

        
class tb_item_click(models.Model):
    item = models.ForeignKey(tb_item,verbose_name="项目id",null=False)
    
    itcl_id = models.IntegerField("项目分类id",null = False)
    click_counter = models.IntegerField("点击率",null = False,default=0)
    class Meta:
        verbose_name = '项目点击表'
        verbose_name_plural = '项目点击表'
    def __str__(self):
        return '项目id  '+str(self.item.item_id)+'  '+'关于                       '+str(self.item.item_name)+'                       的点击表'
        
        
class tb_item_pa(models.Model):
    ipa_id = models.IntegerField('ID', primary_key=True,null=False)
    ipa_name = models.CharField('机构名称',max_length=100,null=False)
    ipa_parent_id = models.IntegerField('所属上级机构的id',null=False)
    ipa_sort = models.IntegerField('排序',null=False)
    area_id = models.IntegerField('机构对应地区的id',null=False)
    ipa_address = models.CharField('发布机构地址',max_length=1000,null=False,default='默认地址')#为了导航到该机构添加
    class Meta:
        verbose_name = '项目发布机构表'
        verbose_name_plural = '项目发布机构表'
    def __str__(self):   #python 2
        return self.ipa_name

class tb_shoucang_item(models.Model):

    user_id = models.IntegerField('对应用户的ID',null=False)
    item_id = models.IntegerField('对应项目的ID',null=False)

class tb_shoucang_goods(models.Model):

    user_id = models.IntegerField('对应用户的ID',null=False)
    goods_id = models.IntegerField('对应服务的ID',null=False)




class tb_area(models.Model):
    area_id = models.IntegerField("地区id",primary_key=True,null=False)
    area_name = models.CharField("地区名称",max_length =100, null = False)
    area_parent_id = models.IntegerField("地区上一级id",null = False)
    area_sort = models.IntegerField("地区排序",null = False,default=0)
    area_deep = models.IntegerField("地区深度",null = False,default=0)
    class Meta:
        verbose_name = '地区表'
        verbose_name_plural = '地区表'
    def __str__(self):
        return self.area_name



class tb_item_class(models.Model):
    itcl_id = models.IntegerField('ID', primary_key=True,null=False)
    itcl_code = models.IntegerField('分类标识码',null=False)
    itcl_name = models.CharField('分类名称',max_length=100,null=False)
    itcl_des = models.CharField('分类描述',max_length=100,null=False)
    necl_parent_id = models.IntegerField('父类ID',null=False)
    necl_sort = models.IntegerField('排序',null=False)
    class Meta:
        verbose_name = '项目分类'
        verbose_name_plural = '项目分类'
    def __str__(self):   #python 2
        return self.itcl_name


class tb_article(models.Model):
    article_id = models.IntegerField('ID', primary_key=True,null=False)
    article_code = models.IntegerField('文章编码',null=False)
    article_name = models.CharField('文章名称',max_length=100,null=False)
    author = models.CharField('文章作者',max_length=100,null=False)
    author_email = models.CharField('作者邮箱',max_length=100,null=False)

    ITEM = 0
    GOODS = 1
    NEWS = 2
    NOTICE =3
    OTHER = 4
    ARTICLE_TYPE = (
    (ITEM,'项目'),
    (GOODS,'商品'),
    (NEWS,'新闻'),
    (NOTICE,'公告'),
    (OTHER,'其他'),
    
    )
    
    article_type = models.IntegerField('文章所属类型',choices=ARTICLE_TYPE,default=ITEM,null=False,blank=False)
    affiliation_id = models.IntegerField('文章的归属id',null=False)
    article_content = models.TextField('文章内容',null=False)
    article_keywords = models.TextField('文章关键字',null=False)
    article_des = models.CharField('文章描述',max_length=100,null=False)
    article_sort = models.IntegerField('排序',null=False)
    upload_time = models.DateTimeField('文章上传时间',auto_now =True,null = False)

    NOTDEFAULT = 0
    ISDEFAULT = 1
   
    IS_DEFAULT = (
    (ISDEFAULT,'默认'),
    (NOTDEFAULT,'非默认'),
    
    )
    is_default = models.IntegerField('是否为默认文章',choices=IS_DEFAULT,default=ISDEFAULT,null=False,blank=False)
    article_click = models.IntegerField('文章点击数',null=False)
    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = '文章表'
    def __str__(self):   #python 2
        return self.article_name
  

class tb_album(models.Model):
    album_id = models.IntegerField('ID', primary_key=True,null=False)
    album_name = models.CharField('相册名称',max_length=40,null=False)

    ITEM = 0
    GOODS = 1
    NEWS = 2
    NOTICE =3
    OTHER = 4
    ALBUM_TYPE = (
    (ITEM,'项目'),
    (GOODS,'商品'),
    (NEWS,'新闻'),
    (NOTICE,'公告'),
    (OTHER,'其他'),
    
    )
    album_type = models.IntegerField('相册类型',choices=ALBUM_TYPE,default=ITEM,null=False,blank=False)

    affiliation_id = models.IntegerField('相册的归属id',null=False)
    nacl_des = models.CharField('相册描述',max_length=100,null=False)
    nacl_sort = models.IntegerField('排序',null=False)
    upload_time = models.DateTimeField('相册建立时间',auto_now = True,null = False)

    NOTDEFAULT = 0
    ISDEFAULT = 1
   
    IS_DEFAULT = (
    (ISDEFAULT,'默认'),
    (NOTDEFAULT,'非默认'),
    
    )

    is_default = models.IntegerField('是否为默认相册',choices=IS_DEFAULT,default=ISDEFAULT,null=False,blank=False)
    class Meta:
        verbose_name = '相册表'
        verbose_name_plural = '相册表'
    def __str__(self):   #python 2
        return self.album_name


class tb_pic(models.Model):
    pic_id = models.IntegerField('ID', primary_key=True,null=False)
    pic_name = models.CharField('图片名称',max_length=40,null=False)
    pic_tag = models.CharField('图片标签',max_length=40,null=False)
    album_id = models.IntegerField('相册id',null=False)
    pic_object = models.ImageField('图片文件',upload_to='img_for_items/%Y/%m/%d',null = False,default="img_for_items/none/no_img.jpg")   
    pic_size = models.IntegerField('项目ID',null=False,default=0)
    upload_time = models.DateTimeField('图片上传时间',auto_now = True,null = False)
    class Meta:
        verbose_name = '图片表'
        verbose_name_plural = '图片表'
    def __str__(self):   #python 2
        return self.pic_name


class tb_accessory(models.Model):
    anne_id=models.IntegerField('ID',null = False)
    comm_id=models.IntegerField('商品ID',null = False)
    apubdate=models.IntegerField('附件上传时间',null = False)
    apublisher = models.CharField('附件上传者',max_length=2,null =False)
    aposition= models.CharField('附件位置',max_length=10,null =False)
    aaddtion= models.CharField('备注',max_length=50)
    class Meta:
        verbose_name = '其他附件表'
        verbose_name_plural = '其他附件表'
    def __unicode__(self):   #python 2 
        return self.apublisher


class tb_Artificial_Representations(models.Model):
    arre_id = models.AutoField('ID',primary_key = True)
    arre_title = models.CharField('申诉标题',max_length = 100, null = False)#申诉标题
    arre_content = models.TextField('申诉内容',max_length = 1000, null = False)#申诉内容
    user_id = models.IntegerField('申诉人名称',null = False)#申诉人id
    user_name = models.CharField('申诉人名称',max_length = 100, null = False)#申诉人名称

    NOTACCEPT = 0
    ACCEPT = 1
    SOLVED = 2
    ARRE_STATE = (
    (NOTACCEPT,'未受理'),
    (ACCEPT,'已受理'),
    (SOLVED,'已解决'),
    
    )
    arre_state = models.IntegerField('申述状态',choices=ARRE_STATE,default=NOTACCEPT,null=False,blank=False)#申述状态0：未受理  1：已受理   2：已解决
    create_time = models.DateTimeField('提交申请时间')
    class Meta:
        verbose_name = '人工申述表'
        verbose_name_plural = '人工申述表'
    def __unicode__(self):   #python 2 
        return self.arre_title

class tb_Message(models.Model):
    mess_id = models.IntegerField(primary_key = True)
    send_id = models.IntegerField(null = False)#发送方ID
    rec_id = models.IntegerField(null = False)#接受方ID
    text_id = models.IntegerField(null = False)#文本ID
    status = models.IntegerField(null = False)#消息状态
    class Meta:
        verbose_name = '站内短信表'
        verbose_name_plural = '站内短信表'

    
class tb_MessageText(models.Model):
    text_id = models.IntegerField(primary_key = True)
    mete_title = models.CharField(max_length = 10, null = False)#短信标题
    mete_content = models.CharField(max_length = 300, null = False)#短信内容
    mete_time = models.DateTimeField('消息发送时间')
    class Meta:
        verbose_name = '站内短信内容表'
        verbose_name_plural = '站内短信内容表'
    def __unicode__(self):
        return self.mete_title  
    
class tb_SysMessage(models.Model):
    sys_id = models.IntegerField(primary_key = True)
    cust_id = models.IntegerField(null = False)#客户ID
    mess_id = models.IntegerField(null = False)#短信ID
    sys_status = models.IntegerField(null = False)#消息状态，0/1：已读/未读    
    class Meta:
        verbose_name = '系统信息表'
        verbose_name_plural = '系统信息表'
class tb_goods_wfc(models.Model):
    goods_id = models.AutoField("自增索引id主键",primary_key = True,null=False)
    goods_name = models.CharField("服务名称",max_length = 40, null = False)
    item_id = models.IntegerField("服务对应项目的id",null = False)
    sp_id = models.IntegerField("服务对应的服务提供商",null = False)
    goods_fanli = models.CharField("平台返利",null=False,max_length=20)
	#smod = models.CharField("服务模式",max_length=20,null=True)
    fea = models.CharField("服务特色",max_length = 1000, null = True)
    cont = models.CharField("服务内容",max_length = 100, null = True)
    steps = models.CharField("服务流程",max_length = 100, null = True)
    exa = models.CharField("成功案例",max_length = 100, null = True)
    smod = models.CharField("服务模式",max_length = 100, null = True)
    goods_payahead = models.IntegerField("首付金额",null=False,default=100)
    goods_awardafter = models.IntegerField("申报成功后奖金",null=True)
    goods_awardmid = models.IntegerField("中期奖金",null=True)
    class Meta:
        verbose_name = '待测服务信息表'
        verbose_name_plural = '待测服务信息表'
    
    def __unicode__(self):
        return self.goods_name



class tb_goods(models.Model):
    goods_id = models.AutoField("自增索引id主键",primary_key = True,null=False)
    item_id = models.IntegerField("服务对应项目的id",null = False)
    sp_id = models.IntegerField("服务对应的服务提供商",null = False)
    goods_area = models.CharField("所在地",max_length = 40,null = False,default="北京")
    goods_name = models.CharField("服务名称",max_length = 40, null = False)
    goods_market_price = models.IntegerField("服务价格",null = False)
    #Addby YZ为了服务列表的数据呈现
    goods_code = models.IntegerField("服务编号",null=True)
    goods_payahead = models.IntegerField("首付金额",null=False,default=100)
    goods_awardafter = models.IntegerField("申报成功后奖金",null=True)
    goods_awardmid = models.IntegerField("中期奖金",null=True)
    goods_accept_starttime = models.DateTimeField("开始接单时间",null=True)
    goods_accept_endtime = models.DateTimeField("最后接单时间",null=True)

    goods_price = models.IntegerField("服务未打折扣报价(标价)",null = False)
    goods_price_discouint = models.FloatField("折扣（标价乘以折扣等于实际成交价）",null = False)
    goods_pay = models.IntegerField("该服务支持的支付方式",null = False)
    goods_guarantee = models.CharField("商家保证",max_length = 100, null = False)
    goods_sort = models.IntegerField("排序",null = False)#用来排序

  	#smod = models.CharField("模式选择",max_length = 20, null = True)
    fea = models.CharField("服务特色",max_length = 20, null = True)
    cont = models.CharField("服务内容",max_length = 100, null = True)
    steps = models.CharField("服务流程",max_length = 100, null = True)
    exa = models.CharField("成功案例",max_length = 100, null = True)
    smod = models.CharField("服务模式",max_length = 100, null = True)
    goods_fanli = models.CharField("平台返利",null=False,max_length=20)
    
    NOTCOMMEND = 0
    COMMEND = 1
    GOODS_COMMEND = (
    (NOTCOMMEND,'不推荐'),
    (COMMEND,"推荐"),
    
    )
    goods_commend = models.IntegerField("是否推荐此服务交易",choices=GOODS_COMMEND,default=NOTCOMMEND,null=False,blank=False)
    goods_evaluation_good_star = models.IntegerField("好评星级",null = False)
    goods_evaluation_count = models.IntegerField("评价数",null = False)
    
    SHOW = 1
    NOTSHOW = 0
    GOODS_SHOW_CHOICES = (
    (SHOW,'显示'),
    (NOTSHOW,"不显示"),
    
    )
    goods_show = models.IntegerField("商品显示状态",choices=GOODS_SHOW_CHOICES,default=SHOW,null=False,blank=False)


    NOTSERVE = 0
    SERVE = 1
    TEMPORARY=2
    GOODS_STATUS_CHOICES = (
    (NOTSERVE,'不可服务'),
    (SERVE,"可服务"),
    (TEMPORARY,"暂时不可服务"),
    )
    goods_status = models.IntegerField("服务提供商服务状态",choices=GOODS_STATUS_CHOICES,default=NOTSERVE,null=False,blank=False)
    class Meta:
        verbose_name = '服务商信息表'
        verbose_name_plural = '服务商信息表'
    
    def __unicode__(self):
        return self.goods_name


    
class tb_goods_click(models.Model):
    goods_id = models.IntegerField("服务商品id",null=False)
    goods_name = models.CharField("服务商品名称",max_length =100, null = False)
    gocl_id = models.IntegerField("服务商品分类id",null = False)
    gocl_num = models.IntegerField("点击率状态",null = False,default=0)
    class Meta:
        verbose_name = '服务商点击表'
        verbose_name_plural = '服务商点击表'
    def __str__(self):
        return self.goods_name


class tb_goods_class(models.Model):
    gocl_id = models.IntegerField("自增主键",primary_key = True,null=False)
    gocl_code = models.IntegerField("分类标示码",null = False)
    gocl_name = models.CharField("分类名称",max_length = 40, null = False)
    gocl_des = models.CharField("分类描述",max_length =100, null = False)
    gocl_sort = models.IntegerField("排序",null = False)
    gocl_parent_id = models.IntegerField("父分类id",null = False)
    class Meta:
        verbose_name = '服务商分类表'
        verbose_name_plural = '服务商分类表'
    def __unicode__(self):
        return self.gocl_name

    def __unicode__(self):
        return self.gocl_des


class tb_goods_evaluation(models.Model):
    goev_id = models.IntegerField("自增索引id主键",primary_key = True,null=False)
    order_id = models.IntegerField("订单id",null = False)
    goods_id = models.IntegerField("评价对应的服务交易的id",null = False)
    goods_name = models.CharField("服务商品的名称",max_length = 100, null = False)
    user_id = models.IntegerField("评价对应的购买者id",null = False)
    user_name = models.CharField("评价对应的购买者name",max_length = 100, null = False)
    create_time = models.DateTimeField("评价日期",auto_now =True,null=False)
    goev_desccredit = models.IntegerField("描述相符评分",null = False)
    goev_servicecredit = models.IntegerField("服务态度评分",null = False)
    goev_content = models.TextField("评价内容",null=False)
    is_anonymous  = models.IntegerField("是否匿名评价",null = False)

    service_provider = models.CharField("对应服务商",max_length = 100, null = True)

    star = models.IntegerField("总体评分",null = True)
    reply_content = models.TextField("回复内容",null=True)
    location = models.CharField("所在地域",max_length = 100, null = True)
    SHOW = 1
    NOTSHOW = 0
    GOEV_SHOW_CHOICES = (
    (SHOW,'显示'),
    (NOTSHOW,"不显示"),
  
    )
    goev_show = models.IntegerField("是否显示",choices=GOEV_SHOW_CHOICES,default=NOTSHOW,null=False,blank=False)
    
    MALICE = 0
    NORMAL= 1
    OTHER=2
    GOEV_STATUS_CHOICES = (
    (MALICE,'恶意评价'),
    (NORMAL,"正常"),
    (OTHER,"其他"),
    )
    goev_status = models.IntegerField("评价状态",choices= GOEV_STATUS_CHOICES,default=MALICE,null=False,blank=False)
    class Meta:
        verbose_name = '服务商评价表'
        verbose_name_plural = '服务商评价表'
    def __str__(self):
        return self.goods_name

    def __str__(self):
        return self.user_name

class tb_order(models.Model):
    order_id = models.IntegerField("自增索引id主键",primary_key = True,null=False)
    order_no = models.IntegerField('订单编号',null=False)
    goods_id = models.IntegerField("商品id",null = False)
    pay_no = models.IntegerField("支付单号",null = False)
    item_id = models.IntegerField("项目id",null = False)
    item_name = models.CharField("项目名称",max_length = 1000, null = False)
    sp_id = models.IntegerField("服务提供商id",null = False)
    sp_name = models.CharField("服务提供商名称",max_length = 40, null = False)
    buyer_id = models.IntegerField("买家id",null = False)
    buyer_name = models.CharField("买家姓名",max_length = 40, null = False)
    buyer_email = models.EmailField("买家电子邮箱",max_length = 40,null=False,blank=False)
    add_time = models.DateTimeField("订单生成时间",auto_now=True,blank=False)
    promise_finish_time = models.DateTimeField("订单截止交付时间", auto_now=True, blank=False)

    efile_send = models.IntegerField("电子档是否提交",null=False,default=0)
    paper_send = models.IntegerField("纸质档是否提交",null=False,default=0)

    payment_code = models.CharField("支付方式名称代码",max_length = 100,null = False)
    has_pay = models.IntegerField("是否支付",null=False,default=0)
    finish_percentage = models.IntegerField('完成进度',null=False,default=0)

    payment_time = models.DateTimeField("支付(付款)时间",null=True,blank=False)#这个需要后续完成
    final_time = models.DateTimeField("订单完成时间",null=True,blank=False)#这个也是后续完成
    good_amount = models.IntegerField("商品总价格",null = False)#服务总价格=首付
    order_amount = models.IntegerField("订单总价格",null = False,default=0)#订单总价格=首付加奖金
    refund_amount = models.IntegerField("退款金额",null = False)#退的钱应该是首付价格
    delay_time = models.DateTimeField("延迟时间",null=True,blank=False)#这个应该是一个时间段的字段

    WEB = 1
    MOBILE = 0
    ORDER_FROM = (
    (WEB,'PC端'),
    (MOBILE,"手机端"),
  
    )

    order_from = models.IntegerField("WEB或者mobile",choices=ORDER_FROM,default=WEB,null=False,blank=False)
    express_id = models.IntegerField("物流公司id",null = False) 
    express_no = models.CharField("物流单号",max_length = 100,null = False) 

    EVALUATE = 1
    NOTEVALUATE = 0
    EVAL_STATE_CHOICES = (
    (NOTEVALUATE,'未评价'),
    (EVALUATE,"已评价"),
  
    )
    eval_state= models.IntegerField("评价状态",choices=EVAL_STATE_CHOICES,default=NOTEVALUATE,null=False,blank=False)
    
    CANCEL= 0
    NOTPAYMENT= 1
    PAYMENT= 2
    DELIVER= 3
    RECEIPT= 4
    ORDER_STATE_CHOICES = (
    (CANCEL,'已取消'),
    (NOTPAYMENT,"未付款"),
    (PAYMENT,'已付款'),
    (DELIVER,"已下单"),#代表生成了订单，后续的付款也没有执行
    (RECEIPT,"已完成"),
    )
    order_state = models.IntegerField("订单状态",choices=ORDER_STATE_CHOICES,default=NOTPAYMENT,null=False,blank=False)

    NOTREFUND = 0
    PARTREFUND = 1
    ALLREFUND = 2
    REFUND_STAT_CHOICES = (
    (NOTREFUND,'无退款'),#代表没有申请退款
    (PARTREFUND,"部分退款"),
    (ALLREFUND,"全部退款"),
  
    )
    refund_state = models.IntegerField("退款状态",choices=REFUND_STAT_CHOICES,default= NOTREFUND,null=False,blank=False)
   
    NORMAL = 0
    LOCK = 1
    LOCK_STAT_CHOICES = (
    (NORMAL,'正常'),
    (LOCK,"锁定"),
  
    )
    lock_state = models.IntegerField("锁定状态",choices=LOCK_STAT_CHOICES,default= NORMAL,null=False,blank=False)
    
    DELIVER= 1
    RECEIPT= 2
    NOTRECEIPT= 3
    HAVERECEIPT= 4
    EXPRESS_STATE_CHOICES = (
    (DELIVER,'待发货'),
    (RECEIPT,"待收货"),
    (NOTRECEIPT,'已付款'),
    (HAVERECEIPT,"已发货"),
    )
    express_state = models.IntegerField("物流状态",choices=EXPRESS_STATE_CHOICES,default= DELIVER,null=False,blank=False)
    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = '订单表'
    
    def __str__(self):
        return self.item_name
      
    
#还未激活的代码
class tb_companyuser(models.Model):
    companyUserId = models.AutoField("用户id",primary_key = True)
    companyUserName = models.CharField("用户名",max_length=100,null=False,blank=False)
    companyUserPassword = models.CharField("密码",max_length=100,null=False,blank=False)
    companyUserCompanyName = models.CharField("公司名称",max_length=100,null=False,blank=False)
    companyUserCompanyLocation = models.CharField("公司位置",max_length=100,null=False,blank=False)#省市县
    companyUserCompanyAddress = models.CharField("公司地址",max_length=100,null=False,blank=False)
    companyUserCompanyCapital = models.CharField("注册资本",max_length=100,null=False,blank=False)
    companyUserCompanyPeople = models.CharField("公司人数",max_length=100,null=False,blank=False)
    companyUserCompanyIndustry = models.CharField("公司行业",max_length=100,null=False,blank=False)
    companyUserCompanyNature = models.CharField("公司性质",max_length=100,null=False,blank=False)
    companyUserContactName = models.CharField("联系人姓名",max_length=40,null=False,blank=False)
    companyUserPhone = models.CharField("固话", max_length=40, null=False, blank=False)#固话
    companyUserTelephone = models.CharField("手机", max_length=40, null=False, blank=False)#手机
    companyUserEmail = models.EmailField("用户邮箱", null=False, blank=False)

    def __unicode__(self):
        return self.companyUserName
    def __unicode__(self):
        return self.companyUserCompanyName
    def __unicode__(self):
        return self.companyUserContactName
        
        
class tb_customcompany(models.Model):
    company_id = models.CharField("企业id",max_length=100,null=False,blank=False,primary_key=True)
    custom_hangye = models.CharField("行业",max_length=100,null=False,blank=False)
    custom_bumen = models.CharField("部门",max_length=100,null=False,blank=False)
    custom_jiebie = models.CharField("级别",max_length=100,null=False,blank=False)
    wanted_guquan = models.CharField("股权",max_length=100,null=False,blank=False)
    wanted_rongzi = models.CharField("债券",max_length=100,null=False,blank=False)
    wanted_ziben = models.CharField("资本",max_length=100,null=False,blank=False)
    self_des = models.CharField("自评",max_length=100,null=True,blank=False)
    item_des = models.CharField("项目评价",max_length=100,null=True,blank=False)
    self_file = models.FileField(upload_to = './upload',null=True)
    item_file = models.FileField(upload_to = './upload',null=True)
    conclusion = models.CharField("网站评价",max_length=100,null=True,blank=False)

class tb_balist(models.Model):
	ba_id = models.AutoField("结算id",primary_key = True)
	order_no = models.IntegerField('订单编号',null=False)
	shangjia = 0
	peitao =1
	BA_K_CHOICES = (
	(shangjia,"商家服务"),
	(peitao,"配套服务"),
	)
	ba_belong = models.IntegerField("服务分类",choices=BA_K_CHOICES,null=False,default= shangjia)
	NotOK = 0
	Gok = 1
	Bok = 2
	Ok	= 3
	BA_STAT_CHOICES = (
	(NotOK,'已下单'),
	(Gok,"客户已确认"),
	(Bok,'商家已确认'),
	(Ok,"已完成"),
	)
	ba_sta = models.IntegerField("结算状态",choices=BA_STAT_CHOICES,default= NotOK,null=False,blank=False)
	ba_time = models.DateTimeField("结算时间",null=True,blank=False,default=None)
	ba_ftime = models.DateTimeField("验单时间",null=True,blank=False,default=None)

#YZ for the back
class tb_back_user(models.Model):
    user_id = models.AutoField("用户id", primary_key=True)

    user_name = models.CharField("用户名称", max_length=100, null=False, blank=False)
    user_password = models.CharField("密码", max_length=100, null=False, blank=False)
    user_telephone = models.CharField("电话", max_length=40, null=False, blank=False)
    user_email = models.EmailField("用户邮箱", null=False, blank=False)

    PASSAUTH = 1
    NOTPASSAUTH = 0
    USER_AUTH_CHOICES = (
        (PASSAUTH, '通过验证'),
        (NOTPASSAUTH, "验证没有通过或者没有验证"),

    )
    user_auth = models.IntegerField("用户验证状态", choices=USER_AUTH_CHOICES,
                                    default=NOTPASSAUTH)  # 用户验证状态0：验证没有通过或者没有验证1：验证通过

    Kefu = 2
    Shenhe = 1
    super_admin = 0
    User_Type_CHOICES = (
        (Kefu, '客服人员'),
        (Shenhe, '审核人员'),
        (super_admin, '超级管理员'),
    )
    user_type = models.IntegerField("注册用户类型", choices=User_Type_CHOICES, default=Kefu)

    class Meta:
        verbose_name = '后台用户'
        verbose_name_plural = '后台用户'

    def __unicode__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_email

    def __unicode__(self):
        return self.user_telephone

    # 用于政资分享的模块--xy


class shareinformation(models.Model):
        projectname = models.CharField("项目名称", max_length=20, null=False)
        projectdirect = models.CharField("项目方向和领域", max_length=20, null=False)
        projectneed = models.CharField("项目申报要求", max_length=30, null=False)
        projectprocess = models.TextField("项目申报流程", null=False)
        projectmanage = models.CharField("项目管理部门", max_length=20, null=False)
        projectlink = models.CharField("项目联系人及电话", max_length=20, null=False)
        LEVEL_CHOICES = (
            ('N1', 'YES'),
            ('N2', 'NO'),
        )
        projectsecret = models.CharField("项目是否保密", max_length=10, null=False, choices=LEVEL_CHOICES)

        class Meta:
            verbose_name = u'政资信息共享'
            verbose_name_plural = u'政资信息共享'

        def __unicode__(self):  # python 2
            return self.projectname

    # 用于政资分享的模块--xy

class Linker(models.Model):
        linkname = models.CharField("联系人姓名", max_length=20, null=False)
        linkemail = models.EmailField("联系人邮箱", null=False, blank=False)
        linkadress = models.CharField("联系人地址", max_length=30, null=False)
        linktelphon = models.CharField("联系人电话", max_length=11, null=False)
        remarks = models.TextField("备注", null=False)
        LEVEL_CHOICES = (
            ('YES', 'YES'),
            ('NO', 'NO'),
        )

        secret = models.CharField("是否保密", max_length=10, null=False, choices=LEVEL_CHOICES)

        class Meta:
            verbose_name = u'政资信息发布人'
            verbose_name_plural = u'政资信息发布人'

        def __unicode__(self):  # python 2
            return self.linkname



class push_info(models.Model):
    push_item_id = models.IntegerField('推送项目的id',null=False)
    push_to_user = models.IntegerField('推送到的用户的id',null=False)

