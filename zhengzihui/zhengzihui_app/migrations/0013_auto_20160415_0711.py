# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0012_auto_20160415_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_apage_class',
            name='Apcl_id',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_notice_class',
            name='Nocl_id',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True),
        ),
    ]
