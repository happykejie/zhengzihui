# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='FileAbout',
            field=models.FileField(default=b'default', upload_to=b'file/Product_file/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='Image',
            field=models.ImageField(default=b'img/Ads_img/None/no-img.jpg', upload_to=b'img/Ads_img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Image',
            field=models.ImageField(default=b'img/News_img/None/no-img.jpg', upload_to=b'img/News_img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=b'img/Product_img/None/no-img.jpg', upload_to=b'img/Product_img/%Y/%m/%d'),
        ),
    ]
