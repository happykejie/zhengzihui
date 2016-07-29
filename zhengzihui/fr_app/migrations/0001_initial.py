# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FRequireInfo',
            fields=[
                ('info_id', models.AutoField(serialize=False, verbose_name=b'Information Id', primary_key=True)),
                ('mobile_num', models.CharField(max_length=30, verbose_name=b'Mobile Number')),
                ('require_type', models.CharField(max_length=2, verbose_name=b'Require type', choices=[(b'N1', b'N1'), (b'N2', b'N2'), (b'N3', b'N3')])),
                ('require_describe', models.CharField(max_length=255, verbose_name=b'Require description')),
                ('news_time', models.DateTimeField(auto_now=True, verbose_name=b'Release Data')),
            ],
        ),
    ]
