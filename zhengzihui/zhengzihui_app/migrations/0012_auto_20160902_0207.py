# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0011_auto_20160901_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods_evaluation',
            name='reply_content',
            field=models.TextField(null=True, verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AddField(
            model_name='tb_goods_evaluation',
            name='service_provider',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86'),
        ),
    ]
