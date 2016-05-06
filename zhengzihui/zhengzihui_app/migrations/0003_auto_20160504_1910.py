# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20160503_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_market_price',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
    ]
