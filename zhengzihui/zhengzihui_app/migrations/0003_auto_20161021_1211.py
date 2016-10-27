# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20161021_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_back_user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe7\x99\xbb\xe9\x99\x86', null=True),
        ),
    ]
