# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0010_tb_apage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_apage',
            name='Has_album',
            field=models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xab\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c'),
        ),
    ]
