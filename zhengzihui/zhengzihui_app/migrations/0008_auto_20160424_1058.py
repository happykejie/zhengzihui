# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0007_auto_20160424_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_album',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\xbb\xba\xe7\xab\x8b\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
