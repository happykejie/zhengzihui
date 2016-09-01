# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0004_auto_20160901_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods',
            name='smod',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\xa8\xa1\xe5\xbc\x8f'),
        ),
        migrations.AddField(
            model_name='tb_goods_wfc',
            name='smod',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\xa8\xa1\xe5\xbc\x8f'),
        ),
    ]
