# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0005_auto_20160422_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_album',
            name='nacl_cover',
        ),
        migrations.RemoveField(
            model_name='tb_pic',
            name='is_thumb',
        ),
        migrations.RemoveField(
            model_name='tb_pic',
            name='pic_spec',
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='aaddtion',
            field=models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='anne_id',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='aposition',
            field=models.CharField(max_length=10, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='apubdate',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='apublisher',
            field=models.CharField(max_length=2, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='comm_id',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='affiliation_id',
            field=models.IntegerField(verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe7\x9a\x84\xe5\xbd\x92\xe5\xb1\x9eid'),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='album_name',
            field=models.CharField(max_length=40, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='album_type',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe9\xa1\xb9\xe7\x9b\xae'), (1, b'\xe5\x95\x86\xe5\x93\x81'), (2, b'\xe6\x96\xb0\xe9\x97\xbb'), (3, b'\xe5\x85\xac\xe5\x91\x8a'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='is_default',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xbb\x98\xe8\xae\xa4\xe7\x9b\xb8\xe5\x86\x8c', choices=[(1, b'\xe9\xbb\x98\xe8\xae\xa4'), (0, b'\xe9\x9d\x9e\xe9\xbb\x98\xe8\xae\xa4')]),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='nacl_des',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='nacl_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', max_length=100),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='affiliation_id',
            field=models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84\xe5\xbd\x92\xe5\xb1\x9eid'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_click',
            field=models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_code',
            field=models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xbc\x96\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_content',
            field=models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_des',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_keywords',
            field=models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_type',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x89\x80\xe5\xb1\x9e\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe9\xa1\xb9\xe7\x9b\xae'), (1, b'\xe5\x95\x86\xe5\x93\x81'), (2, b'\xe6\x96\xb0\xe9\x97\xbb'), (3, b'\xe5\x85\xac\xe5\x91\x8a'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='author',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xbd\x9c\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='author_email',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='is_default',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xbb\x98\xe8\xae\xa4\xe6\x96\x87\xe7\xab\xa0', choices=[(1, b'\xe9\xbb\x98\xe8\xae\xa4'), (0, b'\xe9\x9d\x9e\xe9\xbb\x98\xe8\xae\xa4')]),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', max_length=100),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_content',
            field=models.TextField(max_length=1000, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_id',
            field=models.AutoField(serialize=False, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='arre_title',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='user_id',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_artificial_representations',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='is_hot',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x83\xad\xe9\x97\xa8', choices=[(0, b'\xe6\x99\xae\xe9\x80\x9a'), (1, b'\xe7\x83\xad\xe9\x97\xa8'), (2, b'\xe6\x96\xb0\xe5\x87\xba')]),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='is_recommend',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa8\xe8\x8d\x90', choices=[(1, b'\xe6\x8e\xa8\xe8\x8d\x90'), (0, b'\xe4\xb8\x8d\xe6\x8e\xa8\xe8\x8d\x90')]),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='itcl_id',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x88\x86\xe7\xb1\xbbID'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_about',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xad\xa4\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9a\x84\xe6\x94\xaf\xe6\x8c\x81\xe8\xa1\x8c\xe4\xb8\x9a\xe6\x88\x96\xe8\x80\x85\xe9\xa2\x86\xe5\x9f\x9f'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_code',
            field=models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_deadtime',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_from',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9d\xa5\xe6\xba\x90', choices=[(0, b'\xe6\x9c\xac\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x88\xac\xe8\x99\xab\xe8\x8e\xb7\xe5\x8f\x96'), (1, b'\xe4\xbb\x8e\xe5\x8f\x91\xe5\xb8\x83\xe4\xbf\xa1\xe6\x81\xaf\xe8\x8e\xb7\xe5\x8f\x96')]),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_ga',
            field=models.CharField(max_length=40, verbose_name=b'\xe6\x94\xaf\xe6\x8c\x81\xe9\xa2\x9d\xe5\xba\xa6'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_id',
            field=models.IntegerField(unique=True, serialize=False, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_key',
            field=models.TextField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_level',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb5\x84\xe9\x87\x91\xe7\xba\xa7\xe5\x88\xab', choices=[(1, b'\xe5\x8e\xbf\xe7\xba\xa7\xe8\xb5\x84\xe9\x87\x91'), (2, b'\xe5\xb8\x82\xe7\xba\xa7\xe8\xb5\x84\xe9\x87\x91'), (3, b'\xe7\x9c\x81\xe7\xba\xa7\xe8\xb5\x84\xe9\x87\x91'), (4, b'\xe4\xb8\xad\xe5\xa4\xae\xe8\xb5\x84\xe9\x87\x91')]),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_pa_id',
            field=models.IntegerField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9a\x84\xe6\x9c\xba\xe6\x9e\x84\xe7\x9a\x84id'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_publish',
            field=models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_status',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\xad\xa3\xe5\xb8\xb8'), (1, b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\x94\xb3\xe6\x8a\xa5\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xaa\xe6\xad\xa2'), (2, b'\xe5\x86\x85\xe5\xae\xb9\xe6\x9c\x89\xe8\xaf\xaf')]),
        ),
        migrations.AlterField(
            model_name='tb_item',
            name='item_url',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe9\x80\x9a\xe7\x9f\xa5\xe7\x9a\x84\xe5\x8e\x9f\xe6\x96\x87\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='tb_item_class',
            name='itcl_code',
            field=models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='tb_item_class',
            name='itcl_des',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_item_class',
            name='itcl_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_item_class',
            name='necl_parent_id',
            field=models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbID'),
        ),
        migrations.AlterField(
            model_name='tb_item_class',
            name='necl_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_item_pa',
            name='area_id',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\xaf\xb9\xe5\xba\x94\xe5\x9c\xb0\xe5\x8c\xba\xe7\x9a\x84id'),
        ),
        migrations.AlterField(
            model_name='tb_item_pa',
            name='ipa_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_item_pa',
            name='ipa_parent_id',
            field=models.IntegerField(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\x8a\xe7\xba\xa7\xe6\x9c\xba\xe6\x9e\x84\xe7\x9a\x84id'),
        ),
        migrations.AlterField(
            model_name='tb_item_pa',
            name='ipa_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='album_id',
            field=models.IntegerField(verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8cid'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_name',
            field=models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_object',
            field=models.ImageField(upload_to=b'img_for_items', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\x96\x87\xe4\xbb\xb6'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_size',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_tag',
            field=models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4', max_length=100),
        ),
    ]
