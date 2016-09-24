# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_balist_ba_ftime'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_ba_for_merchant_superivisor',
            fields=[
                ('merchant_id', models.AutoField(serialize=False, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6id', primary_key=True)),
                ('merchant_name', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe5\x90\x8d\xe7\xa7\xb0')),
                ('merchant_addr', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe5\x9c\xb0\xe5\x9d\x80')),
                ('merchant_linkman', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba')),
                ('phone_num', models.CharField(max_length=20, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('num_of_orders', models.IntegerField(verbose_name=b'\xe6\x8e\xa5\xe5\x8d\x95\xe6\xac\xa1\xe6\x95\xb0')),
                ('transaction_amount', models.IntegerField(verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe9\x87\x91\xe9\xa2\x9d')),
            ],
        ),
    ]
