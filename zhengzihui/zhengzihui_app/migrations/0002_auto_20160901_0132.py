# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_goods_wfc',
            fields=[
                ('goods_id', models.IntegerField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True)),
                ('goods_name', models.CharField(max_length=40, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('item_id', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9a\x84id')),
                ('sp_id', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86')),
                ('goods_payahead', models.IntegerField(default=100, verbose_name=b'\xe9\xa6\x96\xe4\xbb\x98\xe9\x87\x91\xe9\xa2\x9d')),
                ('goods_awardafter', models.IntegerField(default=100, verbose_name=b'\xe7\x94\xb3\xe6\x8a\xa5\xe6\x88\x90\xe5\x8a\x9f\xe5\x90\x8e\xe5\xa5\x96\xe9\x87\x91')),
                ('feaon', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb21')),
                ('featw', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb22')),
                ('feath', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb23')),
                ('cont', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x86\x85\xe5\xae\xb9')),
                ('steps', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\xb5\x81\xe7\xa8\x8b')),
                ('exa', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x88\x90\xe5\x8a\x9f\xe6\xa1\x88\xe4\xbe\x8b')),
            ],
            options={
                'verbose_name': '\u5f85\u6d4b\u670d\u52a1\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u5f85\u6d4b\u670d\u52a1\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='cont',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='exa',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x88\x90\xe5\x8a\x9f\xe6\xa1\x88\xe4\xbe\x8b'),
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='feaon',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb21'),
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='feath',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb23'),
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='featw',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb22'),
        ),
        migrations.AddField(
            model_name='tb_goods',
            name='steps',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\xb5\x81\xe7\xa8\x8b'),
        ),
    ]
