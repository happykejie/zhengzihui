# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0003_tb_balist_ba_belong'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods',
            name='goods_area',
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=40, verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe5\x9c\xb0'),
        ),
    ]
