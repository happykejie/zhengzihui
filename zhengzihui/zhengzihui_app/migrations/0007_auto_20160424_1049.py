# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_auto_20160423_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_accessory',
            name='aaddtion',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='anne_id',
            field=models.IntegerField(verbose_name=b'ID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='aposition',
            field=models.CharField(max_length=10, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='apubdate',
            field=models.IntegerField(verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='apublisher',
            field=models.CharField(max_length=2, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='comm_id',
            field=models.IntegerField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81ID'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_content',
            field=models.TextField(max_length=1000, verbose_name=b'\xe7\x94\xb3\xe8\xaf\x89\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_id',
            field=models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_state',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x94\xb3\xe8\xbf\xb0\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x9c\xaa\xe5\x8f\x97\xe7\x90\x86'), (1, b'\xe5\xb7\xb2\xe5\x8f\x97\xe7\x90\x86'), (2, b'\xe5\xb7\xb2\xe8\xa7\xa3\xe5\x86\xb3')]),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_title',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb3\xe8\xaf\x89\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='user_id',
            field=models.IntegerField(verbose_name=b'\xe7\x94\xb3\xe8\xaf\x89\xe4\xba\xba\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb3\xe8\xaf\x89\xe4\xba\xba\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
