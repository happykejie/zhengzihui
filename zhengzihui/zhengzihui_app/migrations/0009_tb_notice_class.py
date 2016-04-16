# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0008_auto_20160415_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_Notice_Class',
            fields=[
                ('Nocl_id', models.IntegerField(serialize=False, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True)),
                ('Nocl_code', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81')),
                ('Nocl_name', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Nocl_des', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('Nocl_parent_id', models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbID')),
                ('Notice_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
    ]
