# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0003_tb_shoucang_goods_tb_shoucang_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_shoucang_goods',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tb_shoucang_item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
