# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_balist_ba_ftime'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods_evaluation',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe5\x9c\xb0\xe5\x9f\x9f'),
        ),
    ]
