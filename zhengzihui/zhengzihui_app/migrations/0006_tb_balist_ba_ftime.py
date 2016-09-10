# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0005_tb_balist_ba_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_balist',
            name='ba_ftime',
            field=models.DateTimeField(default=None, null=True, verbose_name=b'\xe9\xaa\x8c\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
