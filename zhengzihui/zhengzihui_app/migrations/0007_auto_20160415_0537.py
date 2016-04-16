# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_time',
            field=models.DateField(verbose_name=b'date published'),
        ),
    ]
