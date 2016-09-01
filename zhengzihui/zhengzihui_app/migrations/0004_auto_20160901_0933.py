# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0003_auto_20160901_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_goods',
            name='feaon',
        ),
        migrations.RemoveField(
            model_name='tb_goods',
            name='feath',
        ),
        migrations.RemoveField(
            model_name='tb_goods',
            name='featw',
        ),
        migrations.RemoveField(
            model_name='tb_goods_wfc',
            name='feaon',
        ),
        migrations.RemoveField(
            model_name='tb_goods_wfc',
            name='feath',
        ),
        migrations.RemoveField(
            model_name='tb_goods_wfc',
            name='featw',
        ),
        migrations.RemoveField(
            model_name='tb_goods_wfc',
            name='goods_awardafter',
        ),
        migrations.RemoveField(
            model_name='tb_goods_wfc',
            name='goods_payahead',
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='fea',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb2'),
        ),
        migrations.AddField(
            model_name='tb_goods_wfc',
            name='fea',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb2'),
        ),
        migrations.AddField(
            model_name='tb_goods_wfc',
            name='goods_fanli',
            field=models.IntegerField(default=100, verbose_name=b'\xe5\xb9\xb3\xe5\x8f\xb0\xe8\xbf\x94\xe5\x88\xa9'),
        ),
    ]
