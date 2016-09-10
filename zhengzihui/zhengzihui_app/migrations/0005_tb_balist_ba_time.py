# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0004_tb_goods_goods_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_balist',
            name='ba_time',
            field=models.DateTimeField(default=None, null=True, verbose_name=b'\xe7\xbb\x93\xe7\xae\x97\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
