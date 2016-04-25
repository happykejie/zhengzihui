# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0004_auto_20160422_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_item',
            name='item_id',
            field=models.AutoField(serialize=False, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID', primary_key=True),
        ),
    ]
