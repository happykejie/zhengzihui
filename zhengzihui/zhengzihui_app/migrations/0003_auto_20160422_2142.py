# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_tb_goods_goods_successrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_pic',
            name='pic_size',
        ),
        migrations.RemoveField(
            model_name='tb_pic',
            name='pic_uri',
        ),
        migrations.AddField(
            model_name='tb_pic',
            name='pic_object',
            field=models.ImageField(default=b'img_for_items/None/no-img.jpg', upload_to=b'img_for_items', verbose_name=b'\xe5\xae\x9a\xe4\xb9\x89\xe4\xb8\xbaimagefield\xe7\x9a\x84\xe5\xaf\xb9\xe8\xb1\xa1'),
        ),
    ]
