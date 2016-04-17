# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0005_auto_20160403_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_accesory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anne_id', models.IntegerField(max_length=10)),
                ('comm_id', models.IntegerField(max_length=10)),
                ('apubdate', models.IntegerField(max_length=10)),
                ('apublisher', models.CharField(max_length=2)),
                ('aposition', models.CharField(max_length=10)),
                ('aaddtion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tb_album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_id', models.IntegerField(max_length=10)),
                ('album_name', models.CharField(max_length=40)),
                ('album_type', models.IntegerField(max_length=3)),
                ('affiliation_id', models.IntegerField(max_length=10)),
                ('nacl_des', models.CharField(max_length=100)),
                ('nacl_sort', models.IntegerField(max_length=3)),
                ('nacl_cover', models.CharField(max_length=100)),
                ('upload_time', models.IntegerField(max_length=10)),
                ('is_default', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='tb_article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_id', models.IntegerField(max_length=10)),
                ('article_name', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=100)),
                ('author_email', models.CharField(max_length=100)),
                ('article_type', models.IntegerField(max_length=3)),
                ('affiliation_id', models.IntegerField(max_length=10)),
                ('article_code', models.IntegerField(null=True)),
                ('article_content', models.TextField()),
                ('article_keywords', models.TextField()),
                ('article_des', models.CharField(max_length=100)),
                ('article_sort', models.IntegerField(max_length=3)),
                ('upload_time', models.IntegerField(max_length=10)),
                ('is_default', models.IntegerField(max_length=1)),
                ('article_click', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tb_pic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_id', models.IntegerField(max_length=10)),
                ('pic_name', models.CharField(max_length=40)),
                ('pic_tag', models.CharField(max_length=40)),
                ('album_id', models.IntegerField(max_length=10)),
                ('pic_uri', models.CharField(max_length=100)),
                ('pic_size', models.IntegerField(max_length=10)),
                ('pic_spec', models.CharField(max_length=100)),
                ('upload_time', models.IntegerField(max_length=10)),
                ('is_thumb', models.BooleanField()),
            ],
        ),
    ]
