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

