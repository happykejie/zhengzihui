# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_companyUser',
            fields=[
                ('companyUserId', models.AutoField(serialize=False, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id', primary_key=True)),
                ('companyUserName', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('companyUserPassword', models.CharField(max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('companyUserCompanyName', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('companyUserCompanyLocation', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbd\x8d\xe7\xbd\xae')),
                ('companyUserCompanyAddress', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x9c\xb0\xe5\x9d\x80')),
                ('companyUserCompanyCapital', models.CharField(max_length=100, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe8\xb5\x84\xe6\x9c\xac')),
                ('companyUserCompanyPeople', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xba\xba\xe6\x95\xb0')),
                ('companyUserCompanyIndustry', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe8\xa1\x8c\xe4\xb8\x9a')),
                ('companyUserCompanyNature', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x80\xa7\xe8\xb4\xa8')),
                ('companyUserContactName', models.CharField(max_length=40, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('companyUserPhone', models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xba\xe8\xaf\x9d')),
                ('companyUserTelephone', models.CharField(max_length=40, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('companyUserEmail', models.EmailField(max_length=254, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\x82\xae\xe7\xae\xb1')),
            ],
        ),
        migrations.RemoveField(
            model_name='tb_item_click',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='tb_item_click',
            name='item_name',
        ),
        migrations.AddField(
            model_name='tb_item_click',
            name='item',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 16, 13, 19, 32, 850162, tzinfo=utc), verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeid', to='zhengzihui_app.tb_item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tb_order',
            name='order_no',
            field=models.IntegerField(default=datetime.datetime(2016, 7, 16, 13, 19, 47, 247369, tzinfo=utc), verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tb_news',
            name='has_album',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8b\xa5\xe6\x9c\x89\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe7\x9b\xb8\xe5\x86\x8c', choices=[(1, b'\xe6\x8b\xa5\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c'), (0, b'\xe6\xb2\xa1\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c')]),
        ),
        migrations.AlterField(
            model_name='tb_news',
            name='new_is_display',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb', choices=[(1, b'\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb')]),
        ),
        migrations.AlterField(
            model_name='tb_news',
            name='new_top',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb', choices=[(1, b'\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb')]),
        ),
        migrations.AlterField(
            model_name='tb_service_provider',
            name='sp_auth',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe8\xae\xa4\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x9c\xaa\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (1, b'\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (2, b'\xe7\xad\x89\xe5\xbe\x85\xe8\xa2\xab\xe8\xae\xa4\xe8\xaf\x81'), (3, b'\xe6\xad\xa3\xe5\x9c\xa8\xe8\xae\xa4\xe8\xaf\x81')]),
        ),
        migrations.AlterField(
            model_name='tb_user',
            name='user_auth',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\xaa\x8c\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe9\x80\x9a\xe8\xbf\x87\xe9\xaa\x8c\xe8\xaf\x81'), (0, b'\xe9\xaa\x8c\xe8\xaf\x81\xe6\xb2\xa1\xe6\x9c\x89\xe9\x80\x9a\xe8\xbf\x87\xe6\x88\x96\xe8\x80\x85\xe6\xb2\xa1\xe6\x9c\x89\xe9\xaa\x8c\xe8\xaf\x81')]),
        ),
        migrations.AlterField(
            model_name='tb_user',
            name='user_type',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe4\xb8\xaa\xe4\xba\xba\xe7\x94\xa8\xe6\x88\xb7'), (1, b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\x94\xa8\xe6\x88\xb7')]),
        ),
    ]
