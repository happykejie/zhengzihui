# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_goods_goods_fanli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_fanli',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xb9\xb3\xe5\x8f\xb0\xe8\xbf\x94\xe5\x88\xa9'),
        ),
        migrations.AlterField(
            model_name='tb_goods_wfc',
            name='goods_fanli',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xb9\xb3\xe5\x8f\xb0\xe8\xbf\x94\xe5\x88\xa9'),
        ),
    ]
