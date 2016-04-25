# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0008_auto_20160424_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_item',
            name='item_deadtime',
            field=models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_publish',
            field=models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
