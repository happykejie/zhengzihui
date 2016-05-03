# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_area',
            fields=[
                ('area_id', models.IntegerField(serialize=False, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xbaid', primary_key=True)),
                ('area_name', models.CharField(max_length=100, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('area_parent_id', models.IntegerField(verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba\xe4\xb8\x8a\xe4\xb8\x80\xe7\xba\xa7id')),
                ('area_sort', models.IntegerField(default=0, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba\xe6\x8e\x92\xe5\xba\x8f')),
                ('area_deep', models.IntegerField(default=0, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba\xe6\xb7\xb1\xe5\xba\xa6')),
            ],
        ),
        migrations.AlterField(
            model_name='tb_order',
            name='order_amount',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x80\xbb\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AlterField(
            model_name='tb_order',
            name='order_state',
            field=models.IntegerField(default=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88'), (1, b'\xe6\x9c\xaa\xe4\xbb\x98\xe6\xac\xbe'), (2, b'\xe5\xb7\xb2\xe4\xbb\x98\xe6\xac\xbe'), (3, b'\xe5\xb7\xb2\xe5\x8f\x91\xe8\xb4\xa7'), (4, b'\xe5\xb7\xb2\xe6\x94\xb6\xe8\xb4\xa7')]),
        ),
    ]
