# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FRequireInfo',
            fields=[
                ('info_id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Information Id')),
                ('mobile_num', models.CharField(max_length=30, verbose_name=b'Mobile Number')),
                ('require_type', models.CharField(choices=[('\u9879\u76ee\u7533\u62a5', '\u9879\u76ee\u7533\u62a5'), ('\u5438\u5f15\u6295\u8d44', '\u5438\u5f15\u6295\u8d44'), ('\u4e89\u53d6\u8d37\u6b3e', '\u4e89\u53d6\u8d37\u6b3e'), ('\u5de5\u5546\u4ee3\u7406', '\u5de5\u5546\u4ee3\u7406'), ('\u8d44\u8d28\u4ee3\u529e', '\u8d44\u8d28\u4ee3\u529e'), ('\u77e5\u8bc6\u4ea7\u6743', '\u77e5\u8bc6\u4ea7\u6743'), ('\u8d22\u52a1\u670d\u52a1', '\u8d22\u52a1\u670d\u52a1'), (b'N1', b'N1')], max_length=30, verbose_name=b'Require type')),
                ('require_describe', models.CharField(max_length=255, verbose_name=b'Require description')),
                ('news_time', models.DateTimeField(auto_now=True, verbose_name=b'Release Data')),
            ],
        ),
        migrations.CreateModel(
            name='sc_album',
            fields=[
                ('album_id', models.IntegerField(primary_key=True, serialize=False, verbose_name=b'ID')),
                ('album_name', models.CharField(max_length=40, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\x90\x8d\xe7\xa7\xb0')),
                ('album_type', models.IntegerField(choices=[(0, b'\xe9\xa1\xb9\xe7\x9b\xae'), (1, b'\xe5\x95\x86\xe5\x93\x81'), (2, b'\xe6\x96\xb0\xe9\x97\xbb'), (3, b'\xe5\x85\xac\xe5\x91\x8a'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')], default=0, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('affiliation_id', models.IntegerField(verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe7\x9a\x84\xe5\xbd\x92\xe5\xb1\x9eid')),
                ('nacl_des', models.CharField(max_length=100, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('nacl_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8c\xe5\xbb\xba\xe7\xab\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_default', models.IntegerField(choices=[(1, b'\xe9\xbb\x98\xe8\xae\xa4'), (0, b'\xe9\x9d\x9e\xe9\xbb\x98\xe8\xae\xa4')], default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xbb\x98\xe8\xae\xa4\xe7\x9b\xb8\xe5\x86\x8c')),
            ],
            options={
                'verbose_name': '\u76f8\u518c\u8868',
                'verbose_name_plural': '\u76f8\u518c\u8868',
            },
        ),
        migrations.CreateModel(
            name='sc_article',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False, verbose_name=b'ID')),
                ('article_code', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xbc\x96\xe7\xa0\x81')),
                ('article_name', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x90\x8d\xe7\xa7\xb0')),
                ('author', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xbd\x9c\xe8\x80\x85')),
                ('author_email', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe9\x82\xae\xe7\xae\xb1')),
                ('article_type', models.IntegerField(choices=[(0, b'\xe9\xa1\xb9\xe7\x9b\xae'), (1, b'\xe5\x95\x86\xe5\x93\x81'), (2, b'\xe6\x96\xb0\xe9\x97\xbb'), (3, b'\xe5\x85\xac\xe5\x91\x8a'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')], default=0, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x89\x80\xe5\xb1\x9e\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('affiliation_id', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x9a\x84\xe5\xbd\x92\xe5\xb1\x9eid')),
                ('article_content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('article_keywords', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x85\xb3\xe9\x94\xae\xe5\xad\x97')),
                ('article_des', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('article_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_default', models.IntegerField(choices=[(1, b'\xe9\xbb\x98\xe8\xae\xa4'), (0, b'\xe9\x9d\x9e\xe9\xbb\x98\xe8\xae\xa4')], default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xbb\x98\xe8\xae\xa4\xe6\x96\x87\xe7\xab\xa0')),
                ('article_click', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u8868',
                'verbose_name_plural': '\u6587\u7ae0\u8868',
            },
        ),
        migrations.CreateModel(
            name='sc_item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID')),
                ('item_type', models.CharField(max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('price', models.CharField(max_length=40, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('start_time', models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('end_time', models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4')),
                ('supplier', models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86')),
                ('item_name', models.CharField(max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('item_details', models.TextField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='sc_item_click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itcl_id', models.IntegerField(default=0, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x88\x86\xe7\xb1\xbbid')),
                ('click_counter', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe7\x8e\x87')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fr_app.sc_item', verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeid')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u70b9\u51fb\u8868',
                'verbose_name_plural': '\u9879\u76ee\u70b9\u51fb\u8868',
            },
        ),
        migrations.CreateModel(
            name='sc_pic',
            fields=[
                ('pic_id', models.IntegerField(primary_key=True, serialize=False, verbose_name=b'ID')),
                ('pic_name', models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pic_tag', models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xa0\x87\xe7\xad\xbe')),
                ('album_id', models.IntegerField(verbose_name=b'\xe7\x9b\xb8\xe5\x86\x8cid')),
                ('pic_object', models.ImageField(default=b'img_for_items/none/no_img.jpg', upload_to=b'img_for_items/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\x96\x87\xe4\xbb\xb6')),
                ('pic_size', models.IntegerField(default=0, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeID')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u8868',
                'verbose_name_plural': '\u56fe\u7247\u8868',
            },
        ),
    ]
