# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0012_auto_20160902_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods_evaluation',
            name='star',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x80\xbb\xe4\xbd\x93\xe8\xaf\x84\xe5\x88\x86'),
        ),
    ]
