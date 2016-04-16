# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0005_auto_20160403_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_Notice',
            fields=[
                ('Notice_id', models.AutoField(serialize=False, primary_key=True)),
                ('Notice_title', models.CharField(max_length=100)),
                ('Article_id', models.IntegerField()),
                ('Notice_time', models.DateTimeField(auto_now_add=True)),
                ('Notice_source', models.CharField(max_length=100)),
                ('Nocl_id', models.IntegerField()),
                ('Notice_sort', models.IntegerField()),
                ('Notice_is_display', models.IntegerField()),
                ('Notice_top', models.IntegerField()),
            ],
        ),
    ]
