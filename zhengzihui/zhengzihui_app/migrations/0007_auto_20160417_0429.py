# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_accesory_tb_album_tb_article_tb_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tb_accesory',
            new_name='tb_accessory',
        ),
    ]
