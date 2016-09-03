# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0013_tb_goods_evaluation_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_goods_evaluation',
            name='reply_content',
            field=models.TextField(null=True, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
