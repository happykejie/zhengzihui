# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0011_auto_20160415_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_Apage_Class',
            fields=[
                ('Apcl_id', models.AutoField(serialize=False, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True)),
                ('Apcl_code', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81')),
                ('Apcl_name', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Apcl_parent_id', models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbID')),
                ('Apcl_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.AlterField(
            model_name='tb_notice_class',
            name='Nocl_id',
            field=models.AutoField(serialize=False, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True),
        ),
    ]
