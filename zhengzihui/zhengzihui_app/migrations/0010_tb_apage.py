# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0009_tb_notice_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_Apage',
            fields=[
                ('Apage_id', models.AutoField(serialize=False, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5ID', primary_key=True)),
                ('Article_id', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0ID')),
                ('Has_album', models.IntegerField(max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xab\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c')),
                ('Apage_time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('Apage_source', models.CharField(max_length=100, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5\xe6\x9d\xa5\xe6\xba\x90')),
                ('Apcl_id', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID')),
                ('Apage_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('Apage_is_display', models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
            ],
        ),
    ]
