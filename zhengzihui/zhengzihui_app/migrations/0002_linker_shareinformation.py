# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkname', models.CharField(max_length=20, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('linkemail', models.EmailField(max_length=254, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe9\x82\xae\xe7\xae\xb1')),
                ('linkadress', models.CharField(max_length=30, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\x9c\xb0\xe5\x9d\x80')),
                ('linktelphon', models.CharField(max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('remarks', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
                ('secret', models.CharField(max_length=10, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbf\x9d\xe5\xaf\x86', choices=[(b'YES', b'YES'), (b'NO', b'NO')])),
            ],
            options={
                'verbose_name': '\u653f\u8d44\u4fe1\u606f\u53d1\u5e03\u4eba',
                'verbose_name_plural': '\u653f\u8d44\u4fe1\u606f\u53d1\u5e03\u4eba',
            },
        ),
        migrations.CreateModel(
            name='shareinformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectname', models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('projectdirect', models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x96\xb9\xe5\x90\x91\xe5\x92\x8c\xe9\xa2\x86\xe5\x9f\x9f')),
                ('projectneed', models.CharField(max_length=30, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x94\xb3\xe6\x8a\xa5\xe8\xa6\x81\xe6\xb1\x82')),
                ('projectprocess', models.TextField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x94\xb3\xe6\x8a\xa5\xe6\xb5\x81\xe7\xa8\x8b')),
                ('projectmanage', models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\xa1\xe7\x90\x86\xe9\x83\xa8\xe9\x97\xa8')),
                ('projectlink', models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\x8f\x8a\xe7\x94\xb5\xe8\xaf\x9d')),
                ('projectsecret', models.CharField(max_length=10, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x98\xaf\xe5\x90\xa6\xe4\xbf\x9d\xe5\xaf\x86', choices=[(b'N1', b'YES'), (b'N2', b'NO')])),
            ],
            options={
                'verbose_name': '\u653f\u8d44\u4fe1\u606f\u5171\u4eab',
                'verbose_name_plural': '\u653f\u8d44\u4fe1\u606f\u5171\u4eab',
            },
        ),
    ]
