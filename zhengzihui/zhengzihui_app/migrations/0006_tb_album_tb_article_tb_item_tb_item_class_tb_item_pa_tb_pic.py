# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0005_auto_20160403_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_album',
            fields=[
                ('album_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('album_name', models.CharField(max_length=40)),
                ('album_type', models.IntegerField()),
                ('affiliation_id', models.IntegerField()),
                ('nacl_des', models.CharField(max_length=100)),
                ('nacl_sort', models.IntegerField()),
                ('nacl_cover', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(auto_now=True, max_length=100)),
                ('is_default', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_article',
            fields=[
                ('article_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('article_code', models.IntegerField()),
                ('article_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('author_email', models.CharField(max_length=100)),
                ('article_type', models.IntegerField()),
                ('affiliation_id', models.IntegerField()),
                ('article_content', models.TextField()),
                ('article_keywords', models.TextField()),
                ('article_des', models.CharField(max_length=100)),
                ('article_sort', models.IntegerField()),
                ('upload_time', models.DateTimeField(auto_now=True, max_length=100)),
                ('is_default', models.IntegerField()),
                ('article_click', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_item',
            fields=[
                ('item_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('item_code', models.CharField(max_length=20)),
                ('item_name', models.CharField(max_length=100)),
                ('itcl_id', models.IntegerField()),
                ('item_level', models.IntegerField()),
                ('item_ga', models.CharField(max_length=40)),
                ('item_pa_id', models.IntegerField()),
                ('item_publish', models.IntegerField()),
                ('item_deadtime', models.IntegerField()),
                ('item_about', models.CharField(max_length=100)),
                ('item_url', models.CharField(max_length=100)),
                ('item_key', models.TextField()),
                ('item_status', models.IntegerField()),
                ('is_hot', models.IntegerField()),
                ('item_from', models.IntegerField(default=0)),
                ('is_recommend', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tb_item_class',
            fields=[
                ('itcl_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('itcl_code', models.IntegerField()),
                ('itcl_name', models.CharField(max_length=100)),
                ('itcl_des', models.CharField(max_length=100)),
                ('necl_parent_id', models.IntegerField()),
                ('necl_sort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_item_pa',
            fields=[
                ('ipa_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('ipa_name', models.CharField(max_length=100)),
                ('ipa_parent_id', models.IntegerField()),
                ('ipa_sort', models.IntegerField()),
                ('area_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tb_pic',
            fields=[
                ('pic_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('pic_name', models.CharField(max_length=40)),
                ('pic_tag', models.CharField(max_length=40)),
                ('album_id', models.IntegerField()),
                ('pic_uri', models.CharField(max_length=100)),
                ('pic_size', models.IntegerField()),
                ('pic_spec', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(auto_now=True, max_length=100)),
                ('is_thumb', models.IntegerField()),
            ],
        ),
    ]
