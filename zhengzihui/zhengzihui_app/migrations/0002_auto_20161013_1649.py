# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-13 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_rongzi_fuwu_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('pic_tag', models.CharField(max_length=40, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xa0\x87\xe7\xad\xbe')),
                ('pic_object', models.ImageField(default=b'img_for_fuwu/none/no_img.jpg', upload_to=b'img_for_fuwu/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\x96\x87\xe4\xbb\xb6')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u8868',
                'verbose_name_plural': '\u56fe\u7247\u8868',
            },
        ),
        migrations.CreateModel(
            name='tb_rongzi_fuwu_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privince', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x9c\x81')),
                ('city', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xb8\x82')),
                ('distr', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8c\xba')),
                ('xianfen', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8e\xbf\xe4\xbb\xbd')),
                ('fuwu_service_code', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe7\xbc\x96\xe5\x8f\xb7')),
                ('fuwu_service_name', models.CharField(max_length=1000, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe8\x9e\x8d\xe8\xb5\x84\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1')),
                ('fuwu_service_payahead', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe9\xa6\x96\xe4\xbb\x98\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('fuwu_service_award', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe5\xae\x8c\xe6\x88\x90\xe5\x90\x8e\xe5\xa5\x96\xe9\x87\x91')),
                ('fuwu_service_start_time', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('fuwu_service_end_time', models.DateTimeField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4')),
                ('fuwu_service_feature', models.CharField(default=b'\xe8\xbf\x98\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa1\xa8\xe6\x98\x8e\xe7\x89\xb9\xe8\x89\xb2', max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x89\xb9\xe8\x89\xb2')),
                ('fuwu_service_short_intro', models.CharField(default=b'\xe8\xbf\x98\xe6\xb2\xa1\xe6\x9c\x89\xe4\xb8\x8a\xe4\xbc\xa0\xe7\xae\x80\xe4\xbb\x8b', max_length=1000, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xae\x80\xe5\x8d\x95\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('fuwu_service_liucheng', models.CharField(default=b'\xe8\xbf\x98\xe6\xb2\xa1\xe6\x9c\x89\xe6\xb5\x81\xe7\xa8\x8b\xe4\xbf\xa1\xe6\x81\xaf', max_length=1000, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\xb5\x81\xe7\xa8\x8b')),
                ('fuwu_click_counter', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x80\xbb\xe9\x87\x8f')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tb_rongzi_fuwu_sp',
            fields=[
                ('privince', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x9c\x81')),
                ('city', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xb8\x82')),
                ('distr', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8c\xba')),
                ('xianfen', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8e\xbf\xe4\xbb\xbd')),
                ('sp_id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'\xe5\x86\x85\xe9\x83\xa8ID')),
                ('sp_name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sp_code', models.IntegerField(null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe7\xbc\x96\xe7\xa0\x81')),
                ('sp_address', models.CharField(max_length=40, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('psw', models.CharField(max_length=40, null=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('tel', models.CharField(max_length=40, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('master', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x93\x85\xe9\x95\xbf\xe9\xa2\x86\xe5\x9f\x9f')),
                ('sp_image1', models.ImageField(null=True, upload_to=b'img/tb_service_provider_sp_img1/%Y/%m/%d', verbose_name=b'\xe6\x94\xbf\xe8\xb5\x84\xe6\xb1\x87\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe8\xaf\x81\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0')),
                ('sp_image2', models.ImageField(null=True, upload_to=b'img/tb_service_provider_sp_img2/%Y/%m/%d', verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe4\xbb\xa3\xe8\xa1\xa8\xe7\x9a\x84\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\xa7\xe7\x85\xa7\xe4\xb8\x8a\xe4\xbc\xa0')),
                ('sp_grade', models.IntegerField(null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe7\xad\x89\xe7\xba\xa7')),
                ('sp_sort', models.IntegerField(null=True, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('area_id', models.CharField(max_length=10, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe6\x89\x80\xe5\x9c\xa8\xe5\x9c\xb0')),
                ('Register_cap', models.IntegerField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe8\xb5\x84\xe9\x87\x91')),
                ('staff_number', models.IntegerField(null=True, verbose_name=b'\xe8\x81\x8c\xe5\x91\x98\xe4\xba\xba\xe6\x95\xb0')),
                ('Annual_totals', models.IntegerField(null=True, verbose_name=b'\xe5\xb9\xb4\xe8\x90\xa5\xe4\xb8\x9a\xe9\xa2\x9d')),
                ('organization_name', models.CharField(max_length=40, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('organization_id', models.IntegerField(null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe4\xbb\xa3\xe7\xa0\x81')),
                ('organization_assets', models.IntegerField(null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe8\xb5\x84\xe4\xba\xa7')),
                ('organization_profile', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xae\x80\xe4\xbb\x8b')),
                ('sp_type', models.CharField(max_length=60, verbose_name=b'\xe5\x90\x88\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('con_name', models.CharField(max_length=30, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('sp_auth', models.IntegerField(choices=[(0, b'\xe6\x9c\xaa\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (1, b'\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (2, b'\xe7\xad\x89\xe5\xbe\x85\xe8\xa2\xab\xe8\xae\xa4\xe8\xaf\x81'), (3, b'\xe6\xad\xa3\xe5\x9c\xa8\xe8\xae\xa4\xe8\xaf\x81')], default=0, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe8\xae\xa4\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81')),
                ('is_recommend', models.IntegerField(choices=[(1, b'\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90(\xe5\xbd\x93\xe6\x9c\x89\xe7\x9b\xb8\xe5\x90\x8c\xe6\x8a\xa5\xe4\xbb\xb7\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xef\xbc\x8c\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe8\x80\x83\xe8\x99\x91\xe6\x8e\xa8\xe8\x8d\x90)'), (0, b'\xe4\xb8\x8d\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90')], default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90')),
            ],
            options={
                'verbose_name': '\u878d\u8d44\u670d\u52a1\u5546',
                'verbose_name_plural': '\u878d\u8d44\u670d\u52a1\u5546',
            },
        ),
        migrations.CreateModel(
            name='tb_rongzi_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privince', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x9c\x81')),
                ('city', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\xb8\x82')),
                ('distr', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8c\xba')),
                ('xianfen', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8e\xbf\xe4\xbb\xbd')),
                ('fuwu_code', models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe7\xbc\x96\xe5\x8f\xb7')),
                ('fuwu_name', models.CharField(max_length=1000, verbose_name=b'\xe8\x9e\x8d\xe8\xb5\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x9a\x84\xe5\x90\x8d\xe5\xad\x97')),
                ('fuwu_provide_money', models.IntegerField(default=0, verbose_name=b'\xe6\xad\xa4\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x8f\xaf\xe6\x8f\x90\xe4\xbe\x9b\xe7\x9a\x84\xe7\x8e\xb0\xe9\x87\x91\xe8\xb5\x84\xe5\x8a\xa9')),
                ('fuwu_start_time', models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('fuwu_end_time', models.DateTimeField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4')),
                ('fuwu_Toptype', models.CharField(max_length=100, verbose_name=b'\xe7\xac\xac\xe4\xb8\x80\xe5\xb1\x82\xe5\x88\x86\xe7\xb1\xbb')),
                ('fuwu_Subtype', models.CharField(max_length=100, verbose_name=b'\xe7\xac\xac\xe4\xba\x8c\xe5\xb1\x82\xe5\x88\x86\xe7\xb1\xbb')),
                ('fuwu_short_intro', models.CharField(default=b'\xe8\xbf\x98\xe6\xb2\xa1\xe6\x9c\x89\xe6\xb7\xbb\xe5\x8a\xa0\xe7\xae\x80\xe4\xbb\x8b', max_length=100, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\x80\xe5\x8d\x95\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('fuwu_liucheng', models.TextField(default=b'\xe7\xad\x89\xe5\xbe\x85\xe6\x9b\xb4\xe6\xad\xa3\xe6\xb5\x81\xe7\xa8\x8b', null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\xb5\x81\xe7\xa8\x8b')),
                ('fuwu_click_counter', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x80\xbb\xe9\x87\x8f')),
                ('fuwu_type_Value', models.IntegerField(default=0, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x9d\x83\xe5\x80\xbc\xef\xbc\x8c\xe7\x94\xa8\xe4\xba\x8e\xe6\x8e\x92\xe5\xba\x8f')),
                ('fuwu_pic_url', models.ManyToManyField(to='zhengzihui_app.tb_rongzi_fuwu_pic')),
                ('fuwu_service', models.ManyToManyField(to='zhengzihui_app.tb_rongzi_fuwu_service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='tb_service_provider',
            name='sp_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name=b'\xe5\x86\x85\xe9\x83\xa8ID'),
        ),
        migrations.AddField(
            model_name='tb_rongzi_fuwu_service',
            name='fuwu_service_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhengzihui_app.tb_rongzi_fuwu_sp', verbose_name=b'\xe8\xaf\xa5\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86'),
        ),
    ]
