# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20160901_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_id',
            field=models.AutoField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_goods_wfc',
            name='goods_id',
            field=models.AutoField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True),
        ),
    ]
