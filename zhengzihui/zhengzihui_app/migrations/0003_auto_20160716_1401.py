# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20160716_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_news',
            name='news_hot',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb', choices=[(1, b'\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb')]),
        ),
        migrations.AlterField(
            model_name='tb_service_provider',
            name='is_recommend',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90', choices=[(1, b'\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90(\xe5\xbd\x93\xe6\x9c\x89\xe7\x9b\xb8\xe5\x90\x8c\xe6\x8a\xa5\xe4\xbb\xb7\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xef\xbc\x8c\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe8\x80\x83\xe8\x99\x91\xe6\x8e\xa8\xe8\x8d\x90)'), (0, b'\xe4\xb8\x8d\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90')]),
        ),
    ]