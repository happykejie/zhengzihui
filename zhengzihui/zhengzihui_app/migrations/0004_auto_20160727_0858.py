# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0003_auto_20160727_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_user',
            name='expand',
            field=models.ForeignKey(verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x89\xa9\xe5\xb1\x95\xe8\xa1\xa8', to='zhengzihui_app.tb_user_expand', null=True),
        ),
    ]
