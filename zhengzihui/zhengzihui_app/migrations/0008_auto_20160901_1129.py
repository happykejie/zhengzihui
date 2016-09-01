# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0007_auto_20160901_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_goods_wfc',
            name='goods_awardafter',
            field=models.IntegerField(default=100, null=True, verbose_name=b'\xe7\x94\xb3\xe6\x8a\xa5\xe6\x88\x90\xe5\x8a\x9f\xe5\x90\x8e\xe5\xa5\x96\xe9\x87\x91'),
        ),
        migrations.AddField(
            model_name='tb_goods_wfc',
            name='goods_payahead',
            field=models.IntegerField(default=100, verbose_name=b'\xe9\xa6\x96\xe4\xbb\x98\xe9\x87\x91\xe9\xa2\x9d'),
        ),
    ]
