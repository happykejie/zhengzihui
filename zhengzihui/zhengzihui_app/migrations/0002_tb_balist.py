# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_balist',
            fields=[
                ('ba_id', models.AutoField(serialize=False, verbose_name=b'\xe7\xbb\x93\xe7\xae\x97id', primary_key=True)),
                ('order_no', models.IntegerField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7')),
                ('ba_sta', models.IntegerField(default=0, verbose_name=b'\xe7\xbb\x93\xe7\xae\x97\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xb7\xb2\xe4\xb8\x8b\xe5\x8d\x95'), (1, b'\xe5\xae\xa2\xe6\x88\xb7\xe5\xb7\xb2\xe7\xa1\xae\xe8\xae\xa4'), (2, b'\xe5\x95\x86\xe5\xae\xb6\xe5\xb7\xb2\xe7\xa1\xae\xe8\xae\xa4'), (3, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
            ],
        ),
    ]
