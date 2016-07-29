#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.

REQUIRE_TYPE = (
    ('N1','N1'),
    ('N2','N2'),
    ('N3','N3'),
)

class FRequireInfo(models.Model):
    info_id = models.AutoField("Information Id", primary_key=True)
    mobile_num = models.CharField("Mobile Number", max_length=30,null=False)
    require_type = models.CharField("Require type", max_length=2,choices=REQUIRE_TYPE,null=False)
    require_describe = models.CharField("Require description", max_length=255)
    news_time = models.DateTimeField("Release Data",auto_now=True)

    def __unicode__(self):
        return self.mobile_num+','+self.require_type

