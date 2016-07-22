# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tb_user',
            old_name='expend',
            new_name='expand',
        ),
    ]
