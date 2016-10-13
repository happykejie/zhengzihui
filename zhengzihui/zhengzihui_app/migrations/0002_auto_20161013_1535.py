# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_service_provider',
            name='sp_id',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe5\x86\x85\xe9\x83\xa8ID', primary_key=True),
        ),
    ]
