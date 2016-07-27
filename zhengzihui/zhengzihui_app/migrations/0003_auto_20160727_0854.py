# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0002_auto_20160722_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_user_expand',
            name='companyUserContactName',
            field=models.CharField(max_length=40, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='companyUserPhone',
            field=models.CharField(max_length=40, null=True, verbose_name=b'\xe5\x9b\xba\xe8\xaf\x9d'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_address',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\xb3\xa8\xe5\x86\x8c\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_district',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe5\x9c\xa8\xe5\x8c\xba\xe5\x8e\xbf'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_industry',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe5\xb1\x9e\xe8\xa1\x8c\xe4\xb8\x9a'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_name',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_nature',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x80\xa7\xe8\xb4\xa8'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_registered_capital',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\xb3\xa8\xe5\x86\x8c\xe8\xb5\x84\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_stuff_no',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xba\xba\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_user_expand',
            name='company_tel',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x94\xb5\xe8\xaf\x9d'),
        ),
    ]
