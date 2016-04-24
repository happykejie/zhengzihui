# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0003_auto_20160422_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_pic',
            name='pic_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_object',
            field=models.ImageField(upload_to=b'img_for_items', verbose_name=b'\xe5\xae\x9a\xe4\xb9\x89\xe4\xb8\xbaimagefield\xe7\x9a\x84\xe5\xaf\xb9\xe8\xb1\xa1'),
        ),
    ]
