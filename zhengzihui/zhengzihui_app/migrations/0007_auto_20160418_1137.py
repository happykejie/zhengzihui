# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0006_tb_album_tb_article_tb_item_tb_item_class_tb_item_pa_tb_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_Apage',
            fields=[
                ('Apage_id', models.AutoField(serialize=False, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5ID', primary_key=True)),
                ('Article_id', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0ID')),
                ('Has_album', models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xab\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c')),
                ('Apage_time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('Apage_source', models.CharField(max_length=100, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5\xe6\x9d\xa5\xe6\xba\x90')),
                ('Apcl_id', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID')),
                ('Apage_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('Apage_is_display', models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
            ],
        ),
        migrations.CreateModel(
            name='Tb_Apage_Class',
            fields=[
                ('Apcl_id', models.IntegerField(serialize=False, verbose_name=b'\xe5\x8d\x95\xe9\xa1\xb5\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True)),
                ('Apcl_code', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81')),
                ('Apcl_name', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Apcl_parent_id', models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbID')),
                ('Apcl_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='tb_News',
            fields=[
                ('news_id', models.AutoField(help_text=b'\xe6\x96\xb0\xe9\x97\xbbid', serialize=False, primary_key=True)),
                ('article_id', models.IntegerField(help_text=b'\xe6\x96\x87\xe7\xab\xa0ID')),
                ('news_time', models.DateTimeField(help_text=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('news_source', models.CharField(help_text=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\x9d\xa5\xe6\xba\x90', max_length=100)),
                ('necl_id', models.IntegerField(help_text=b'\xe5\x88\x86\xe7\xb1\xbbID')),
                ('news_sort', models.IntegerField(help_text=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\x8e\x92\xe5\xba\x8f')),
                ('click_counter', models.IntegerField(help_text=b'\xe6\x80\xbb\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f')),
                ('has_album', models.CharField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8b\xa5\xe6\x9c\x89\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe7\x9b\xb8\xe5\x86\x8c', max_length=20, choices=[(1, b'\xe6\x8b\xa5\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c'), (0, b'\xe6\xb2\xa1\xe6\x9c\x89\xe7\x9b\xb8\xe5\x86\x8c')])),
                ('news_hot', models.CharField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb', max_length=20, choices=[(1, b'\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe7\x83\xad\xe7\x82\xb9\xe6\x96\xb0\xe9\x97\xbb')])),
                ('new_top', models.CharField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb', max_length=20, choices=[(1, b'\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe7\xbd\xae\xe9\xa1\xb6\xe6\x96\xb0\xe9\x97\xbb')])),
                ('new_is_display', models.CharField(default=0, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb', max_length=20, choices=[(1, b'\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb'), (0, b'\xe9\x9d\x9e\xe5\x89\x8d\xe7\xab\xaf\xe5\xb1\x95\xe7\xa4\xba\xe6\x96\xb0\xe9\x97\xbb')])),
            ],
        ),
        migrations.CreateModel(
            name='tb_News_Class',
            fields=[
                ('necl_id', models.AutoField(help_text=b'\xe5\x88\x86\xe7\xb1\xbbid', serialize=False, primary_key=True)),
                ('necl_code', models.IntegerField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81')),
                ('necl_name', models.CharField(help_text=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', max_length=100)),
                ('necl_parent_id', models.IntegerField(help_text=b'\xe7\x88\xb6\xe7\xb1\xbbID')),
                ('necl_sort', models.IntegerField(help_text=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Tb_Notice',
            fields=[
                ('Notice_id', models.AutoField(serialize=False, primary_key=True)),
                ('Notice_title', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x98')),
                ('Article_id', models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0ID')),
                ('Notice_time', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('Notice_source', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\x9d\xa5\xe6\xba\x90')),
                ('Nocl_id', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID')),
                ('Notice_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('Notice_is_display', models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
                ('Notice_top', models.IntegerField(verbose_name=b'\xe5\xbc\xba\xe5\x88\xb6\xe7\xbd\xae\xe9\xa1\xb6')),
            ],
        ),
        migrations.CreateModel(
            name='Tb_Notice_Class',
            fields=[
                ('Nocl_id', models.IntegerField(serialize=False, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID', primary_key=True)),
                ('Nocl_code', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe8\xaf\x86\xe7\xa0\x81')),
                ('Nocl_name', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Nocl_des', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('Nocl_parent_id', models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbID')),
                ('Notice_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='tb_service_provider',
            fields=[
                ('sp_code', models.IntegerField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe7\xbc\x96\xe7\xa0\x81', serialize=False, primary_key=True)),
                ('sp_id', models.IntegerField(help_text=b'\xe5\x86\x85\xe9\x83\xa8ID')),
                ('sp_name', models.CharField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0', max_length=40)),
                ('psw', models.CharField(help_text=b'\xe5\xaf\x86\xe7\xa0\x81', max_length=40)),
                ('tel', models.CharField(help_text=b'\xe7\x94\xb5\xe8\xaf\x9d', max_length=40)),
                ('email', models.EmailField(help_text=b'\xe9\x82\xae\xe7\xae\xb1', max_length=254)),
                ('master', models.CharField(help_text=b'\xe6\x93\x85\xe9\x95\xbf\xe9\xa2\x86\xe5\x9f\x9f', max_length=50)),
                ('sp_image1', models.ImageField(help_text=b'\xe6\x94\xbf\xe8\xb5\x84\xe6\xb1\x87\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe8\xaf\x81\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0', upload_to=b'')),
                ('sp_image2', models.ImageField(help_text=b'\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe4\xbb\xa3\xe8\xa1\xa8\xe7\x9a\x84\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\xa7\xe7\x85\xa7\xe4\xb8\x8a\xe4\xbc\xa0', upload_to=b'')),
                ('sp_grade', models.IntegerField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe7\xad\x89\xe7\xba\xa7')),
                ('sp_sort', models.IntegerField(help_text=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('area_id', models.CharField(help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe6\x89\x80\xe5\x9c\xa8\xe5\x9c\xb0', max_length=10)),
                ('Register_cap', models.IntegerField(help_text=b'\xe6\xb3\xa8\xe5\x86\x8c\xe8\xb5\x84\xe9\x87\x91')),
                ('staff_number', models.IntegerField(help_text=b'\xe8\x81\x8c\xe5\x91\x98\xe4\xba\xba\xe6\x95\xb0')),
                ('Annual_totals', models.IntegerField(help_text=b'\xe5\xb9\xb4\xe8\x90\xa5\xe4\xb8\x9a\xe9\xa2\x9d')),
                ('organization_name', models.CharField(help_text=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0', max_length=40)),
                ('organization_id', models.IntegerField(help_text=b'\xe6\x9c\xba\xe6\x9e\x84\xe4\xbb\xa3\xe7\xa0\x81')),
                ('organization_assets', models.IntegerField(help_text=b'\xe6\x9c\xba\xe6\x9e\x84\xe8\xb5\x84\xe4\xba\xa7')),
                ('organization_profile', models.CharField(help_text=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xae\x80\xe4\xbb\x8b', max_length=100)),
                ('sp_auth', models.CharField(default=0, help_text=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe8\xae\xa4\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81', max_length=20, choices=[(0, b'\xe6\x9c\xaa\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (1, b'\xe9\x80\x9a\xe8\xbf\x87\xe8\xae\xa4\xe8\xaf\x81'), (2, b'\xe7\xad\x89\xe5\xbe\x85\xe8\xa2\xab\xe8\xae\xa4\xe8\xaf\x81'), (3, b'\xe6\xad\xa3\xe5\x9c\xa8\xe8\xae\xa4\xe8\xaf\x81')])),
                ('is_recommend', models.CharField(default=1, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90', max_length=20, choices=[(1, b'\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90(\xe5\xbd\x93\xe6\x9c\x89\xe7\x9b\xb8\xe5\x90\x8c\xe6\x8a\xa5\xe4\xbb\xb7\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xef\xbc\x8c\xe6\x98\xaf\xe5\x90\xa6\xe4\xbc\x98\xe5\x85\x88\xe8\x80\x83\xe8\x99\x91\xe6\x8e\xa8\xe8\x8d\x90)'), (0, b'\xe4\xb8\x8d\xe4\xbc\x98\xe5\x85\x88\xe6\x8e\xa8\xe8\x8d\x90')])),
            ],
        ),
        migrations.CreateModel(
            name='tb_user',
            fields=[
                ('user_id', models.AutoField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7id', serialize=False, primary_key=True)),
                ('user_name', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', max_length=100)),
                ('user_password', models.CharField(help_text=b'\xe5\xaf\x86\xe7\xa0\x81', max_length=100)),
                ('user_telephone', models.CharField(help_text=b'\xe7\x94\xb5\xe8\xaf\x9d', max_length=40)),
                ('user_email', models.EmailField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\x82\xae\xe7\xae\xb1', max_length=254)),
                ('user_auth', models.CharField(default=0, help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\xaa\x8c\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81', max_length=20, choices=[(1, b'\xe9\x80\x9a\xe8\xbf\x87\xe9\xaa\x8c\xe8\xaf\x81'), (0, b'\xe9\xaa\x8c\xe8\xaf\x81\xe6\xb2\xa1\xe6\x9c\x89\xe9\x80\x9a\xe8\xbf\x87\xe6\x88\x96\xe8\x80\x85\xe6\xb2\xa1\xe6\x9c\x89\xe9\xaa\x8c\xe8\xaf\x81')])),
                ('user_type', models.CharField(default=0, help_text=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b', max_length=20, choices=[(0, b'\xe4\xb8\xaa\xe4\xba\xba\xe7\x94\xa8\xe6\x88\xb7'), (1, b'\xe4\xbc\x81\xe4\xb8\x9a\xe7\x94\xa8\xe6\x88\xb7')])),
            ],
        ),
        migrations.CreateModel(
            name='tb_user_expand',
            fields=[
                ('user_id', models.AutoField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7id', serialize=False, primary_key=True)),
                ('company_tel', models.CharField(help_text=b'\xe5\x8a\x9e\xe5\x85\xac\xe7\x94\xb5\xe8\xaf\x9d', max_length=30)),
                ('company_email', models.EmailField(help_text=b'\xe5\x8a\x9e\xe5\x85\xac\xe9\x82\xae\xe7\xae\xb1', max_length=254)),
                ('company_name', models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0', max_length=30)),
                ('company_district', models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe5\x9c\xa8\xe5\x8c\xba\xe5\x8e\xbf', max_length=50)),
                ('company_address', models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\xb3\xa8\xe5\x86\x8c\xe5\x9c\xb0\xe5\x9d\x80', max_length=50)),
                ('company_registered_capital', models.IntegerField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\xb3\xa8\xe5\x86\x8c\xe8\xb5\x84\xe6\x9c\xac')),
                ('company_industry', models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\x80\xe5\xb1\x9e\xe8\xa1\x8c\xe4\xb8\x9a', max_length=30)),
                ('company_stuff_no', models.IntegerField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xba\xba\xe6\x95\xb0')),
                ('company_nature', models.CharField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x80\xa7\xe8\xb4\xa8', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Ads',
        ),
        migrations.RemoveField(
            model_name='book',
            name='back',
        ),
        migrations.RemoveField(
            model_name='book',
            name='content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]