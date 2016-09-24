#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.

REQUIRE_TYPE = (
    (u'项目申报',u'项目申报'),
    (u'吸引投资',u'吸引投资'),
    (u'争取贷款',u'争取贷款'),
    (u'工商代理',u'工商代理'),
    (u'资质代办',u'资质代办'),
    (u'知识产权',u'知识产权'),
    (u'财务服务',u'财务服务'),
    ('N1','N1'),
)

class FRequireInfo(models.Model):
    info_id = models.AutoField("Information Id", primary_key=True)
    mobile_num = models.CharField("Mobile Number", max_length=30,null=False)
    require_type = models.CharField("Require type", max_length=30,choices=REQUIRE_TYPE,null=False)
    require_describe = models.CharField("Require description", max_length=255)
    news_time = models.DateTimeField("Release Data",auto_now=True)

    def __unicode__(self):
        return self.mobile_num+','+self.require_type


####supporting center part#####################################################
# designed by zp
class sc_item(models.Model):
    """这是配套服务中所提供商品的表单。
    图片存放在tb_album,tb_pic中，查找关系为 this.item_id <- tb_album.affiliation_id <- tb_pic.album_id .
    """
    item_id = models.AutoField('项目ID', primary_key=True)
    # 项目类型可选值为： '工商代理','资质代办','知识产权','财务服务'，'其他'
    item_type = models.CharField('项目类型',max_length=20,null=False,blank=False)
    price = models.CharField('价格',max_length=40,null=False)
    start_time = models.DateTimeField('项目发布时间',null=False)
    end_time = models.DateTimeField('项目截止时间',null=False)
    supplier = models.CharField('项目提供商',null=False,max_length=50)
    item_name = models.CharField('项目名称',max_length=100,null=False)
    item_details = models.TextField('项目内容',null=False)


# 这部分主要是摘抄自“服务列表页面”所使用的model
# 下面这部分表是为配套服务设置，由于表没有设计好


class sc_item_click(models.Model):
    item = models.ForeignKey(sc_item,verbose_name="项目id",null=False)
    
    itcl_id = models.IntegerField("项目分类id",null = False,default=0)
    click_counter = models.IntegerField("点击率",null = False,default=0)
    class Meta:
        verbose_name = '项目点击表'
        verbose_name_plural = '项目点击表'
    def __str__(self):
        return '项目id  '+str(self.item.item_id)+'  '+'关于                       '+str(self.item.item_name)+'                       的点击表'

"""
class sc_item_pa(models.Model):
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
"""

class sc_album(models.Model):
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



class sc_pic(models.Model):
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



class sc_article(models.Model):
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




