# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20160402_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='Content',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='ads',
            name='Puton_Stuff',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ads',
            name='Title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='news',
            name='Publish_Editer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='Info',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Puton_Stuff',
            field=models.CharField(max_length=100),
        ),
    ]
