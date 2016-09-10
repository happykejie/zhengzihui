# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_tb_balist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_balist',
            name='ba_belong',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x88\x86\xe7\xb1\xbb', choices=[(0, b'\xe5\x95\x86\xe5\xae\xb6\xe6\x9c\x8d\xe5\x8a\xa1'), (1, b'\xe9\x85\x8d\xe5\xa5\x97\xe6\x9c\x8d\xe5\x8a\xa1')]),
        ),
    ]
