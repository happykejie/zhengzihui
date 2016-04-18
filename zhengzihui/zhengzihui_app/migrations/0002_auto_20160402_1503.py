# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='Image',
            field=models.ImageField(default=b'img/Ads_img/None/no-img.jpg', upload_to=b'img/Ads_img'),
        ),
        migrations.AddField(
            model_name='ads',
            name='Title',
            field=models.CharField(default=b'default', max_length=100),
        ),
        migrations.AddField(
            model_name='news',
            name='Image',
            field=models.ImageField(default=b'img/News_img/None/no-img.jpg', upload_to=b'img/News_img'),
        ),
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=b'img/Product_img/None/no-img.jpg', upload_to=b'img/Product_img'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='Content',
            field=models.CharField(default=b'default', max_length=1000),
        ),
        migrations.AlterField(
            model_name='ads',
            name='Puton_Stuff',
            field=models.CharField(default=b'default', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=models.TextField(default=b'default', max_length=10000),
        ),
        migrations.AlterField(
            model_name='news',
            name='Publish_Editer',
            field=models.CharField(default=b'default', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(default=b'default', max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='Info',
            field=models.CharField(default=b'default', max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(default=b'default', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Puton_Stuff',
            field=models.CharField(default=b'default', max_length=100),
        ),
    ]
