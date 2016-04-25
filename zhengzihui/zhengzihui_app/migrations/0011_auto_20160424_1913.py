# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0010_auto_20160424_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_goods_class',
            fields=[
                ('gocl_id', models.IntegerField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe4\xb8\xbb\xe9\x94\xae', primary_key=True)),
                ('gocl_code', models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe7\xa4\xba\xe7\xa0\x81')),
                ('gocl_name', models.CharField(max_length=40, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('gocl_des', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('gocl_sort', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('gocl_parent_id', models.IntegerField(verbose_name=b'\xe7\x88\xb6\xe5\x88\x86\xe7\xb1\xbbid')),
            ],
        ),
        migrations.CreateModel(
            name='tb_goods_click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_id', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x93\x81id')),
                ('goods_name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('gocl_id', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbbid')),
                ('gocl_num', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe7\x8e\x87\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.CreateModel(
            name='tb_goods_evaluation',
            fields=[
                ('goev_id', models.IntegerField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True)),
                ('order_id', models.IntegerField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95id')),
                ('goods_id', models.IntegerField(verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xa4\xe6\x98\x93\xe7\x9a\x84id')),
                ('goods_name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x93\x81\xe7\x9a\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user_id', models.IntegerField(verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe8\xb4\xad\xe4\xb9\xb0\xe8\x80\x85id')),
                ('user_name', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe8\xb4\xad\xe4\xb9\xb0\xe8\x80\x85name')),
                ('create_time', models.DateTimeField(verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe6\x97\xa5\xe6\x9c\x9f')),
                ('goev_desccredit', models.IntegerField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0\xe7\x9b\xb8\xe7\xac\xa6\xe8\xaf\x84\xe5\x88\x86')),
                ('goev_servicecredit', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x80\x81\xe5\xba\xa6\xe8\xaf\x84\xe5\x88\x86')),
                ('goev_content', models.TextField(verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe5\x86\x85\xe5\xae\xb9')),
                ('is_anonymous', models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8c\xbf\xe5\x90\x8d\xe8\xaf\x84\xe4\xbb\xb7')),
                ('goev_show', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba', choices=[(1, b'\xe6\x98\xbe\xe7\xa4\xba'), (0, b'\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba')])),
                ('goev_status', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x81\xb6\xe6\x84\x8f\xe8\xaf\x84\xe4\xbb\xb7'), (1, b'\xe6\xad\xa3\xe5\xb8\xb8'), (2, b'\xe5\x85\xb6\xe4\xbb\x96')])),
            ],
        ),
        migrations.CreateModel(
            name='tb_order',
            fields=[
                ('order_id', models.IntegerField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True)),
                ('order_no', models.IntegerField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7')),
                ('pay_no', models.IntegerField(verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe5\x8d\x95\xe5\x8f\xb7')),
                ('item_id', models.IntegerField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xaeid')),
                ('item_name', models.CharField(max_length=40, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sp_id', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86id')),
                ('sp_name', models.CharField(max_length=40, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('buyer_id', models.IntegerField(verbose_name=b'\xe4\xb9\xb0\xe5\xae\xb6id')),
                ('buyer_name', models.CharField(max_length=40, verbose_name=b'\xe4\xb9\xb0\xe5\xae\xb6\xe5\xa7\x93\xe5\x90\x8d')),
                ('buyer_email', models.EmailField(max_length=40, verbose_name=b'\xe4\xb9\xb0\xe5\xae\xb6\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1')),
                ('add_time', models.DateTimeField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x94\x9f\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('payment_code', models.CharField(max_length=100, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f\xe5\x90\x8d\xe7\xa7\xb0\xe4\xbb\xa3\xe7\xa0\x81')),
                ('payment_time', models.DateTimeField(verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98(\xe4\xbb\x98\xe6\xac\xbe)\xe6\x97\xb6\xe9\x97\xb4')),
                ('final_time', models.DateTimeField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('good_amount', models.IntegerField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x80\xbb\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('order_amount', models.IntegerField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x80\xbb\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('refund_amount', models.IntegerField(verbose_name=b'\xe9\x80\x80\xe6\xac\xbe\xe9\x87\x91\xe9\xa2\x9d')),
                ('delay_time', models.DateTimeField(verbose_name=b'\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('order_from', models.IntegerField(default=1, verbose_name=b'WEB\xe6\x88\x96\xe8\x80\x85mobile', choices=[(1, b'PC\xe7\xab\xaf'), (0, b'\xe6\x89\x8b\xe6\x9c\xba\xe7\xab\xaf')])),
                ('express_id', models.IntegerField(verbose_name=b'\xe7\x89\xa9\xe6\xb5\x81\xe5\x85\xac\xe5\x8f\xb8id')),
                ('express_no', models.CharField(max_length=100, verbose_name=b'\xe7\x89\xa9\xe6\xb5\x81\xe5\x8d\x95\xe5\x8f\xb7')),
                ('eval_state', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x9c\xaa\xe8\xaf\x84\xe4\xbb\xb7'), (1, b'\xe5\xb7\xb2\xe8\xaf\x84\xe4\xbb\xb7')])),
                ('order_state', models.IntegerField(default=2, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88'), (1, b'\xe6\x9c\xaa\xe4\xbb\x98\xe6\xac\xbe'), (2, b'\xe5\xb7\xb2\xe4\xbb\x98\xe6\xac\xbe'), (3, b'\xe5\xb7\xb2\xe5\x8f\x91\xe8\xb4\xa7'), (4, b'\xe5\xb7\xb2\xe6\x94\xb6\xe8\xb4\xa7')])),
                ('refund_state', models.IntegerField(default=0, verbose_name=b'\xe9\x80\x80\xe6\xac\xbe\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x97\xa0\xe9\x80\x80\xe6\xac\xbe'), (1, b'\xe9\x83\xa8\xe5\x88\x86\xe9\x80\x80\xe6\xac\xbe'), (2, b'\xe5\x85\xa8\xe9\x83\xa8\xe9\x80\x80\xe6\xac\xbe')])),
                ('lock_state', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x81\xe5\xae\x9a\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\xad\xa3\xe5\xb8\xb8'), (1, b'\xe9\x94\x81\xe5\xae\x9a')])),
                ('express_state', models.IntegerField(default=1, verbose_name=b'\xe7\x89\xa9\xe6\xb5\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe5\xbe\x85\xe5\x8f\x91\xe8\xb4\xa7'), (2, b'\xe5\xbe\x85\xe6\x94\xb6\xe8\xb4\xa7'), (3, b'\xe5\xb7\xb2\xe4\xbb\x98\xe6\xac\xbe'), (4, b'\xe5\xb7\xb2\xe5\x8f\x91\xe8\xb4\xa7')])),
            ],
        ),
        migrations.RemoveField(
            model_name='tb_goods',
            name='goods_successrate',
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='album_id',
            field=models.IntegerField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_commend',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa8\xe8\x8d\x90\xe6\xad\xa4\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xa4\xe6\x98\x93', choices=[(0, b'\xe4\xb8\x8d\xe6\x8e\xa8\xe8\x8d\x90'), (1, b'\xe6\x8e\xa8\xe8\x8d\x90')]),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_evaluation_count',
            field=models.IntegerField(verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_evaluation_good_star',
            field=models.IntegerField(verbose_name=b'\xe5\xa5\xbd\xe8\xaf\x84\xe6\x98\x9f\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_guarantee',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe4\xbf\x9d\xe8\xaf\x81'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_id',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe8\x87\xaa\xe5\xa2\x9e\xe7\xb4\xa2\xe5\xbc\x95id\xe4\xb8\xbb\xe9\x94\xae', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_market_price',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_name',
            field=models.CharField(max_length=40, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_pay',
            field=models.IntegerField(verbose_name=b'\xe8\xaf\xa5\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x94\xaf\xe6\x8c\x81\xe7\x9a\x84\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_price',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9c\xaa\xe6\x89\x93\xe6\x8a\x98\xe6\x89\xa3\xe6\x8a\xa5\xe4\xbb\xb7(\xe6\xa0\x87\xe4\xbb\xb7)'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_price_discouint',
            field=models.FloatField(verbose_name=b'\xe6\x8a\x98\xe6\x89\xa3\xef\xbc\x88\xe6\xa0\x87\xe4\xbb\xb7\xe4\xb9\x98\xe4\xbb\xa5\xe6\x8a\x98\xe6\x89\xa3\xe7\xad\x89\xe4\xba\x8e\xe5\xae\x9e\xe9\x99\x85\xe6\x88\x90\xe4\xba\xa4\xe4\xbb\xb7\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_show',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x98\xbe\xe7\xa4\xba\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe6\x98\xbe\xe7\xa4\xba'), (0, b'\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba')]),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='goods_status',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86\xe6\x9c\x8d\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8d\xe5\x8f\xaf\xe6\x9c\x8d\xe5\x8a\xa1'), (1, b'\xe5\x8f\xaf\xe6\x9c\x8d\xe5\x8a\xa1'), (2, b'\xe6\x9a\x82\xe6\x97\xb6\xe4\xb8\x8d\xe5\x8f\xaf\xe6\x9c\x8d\xe5\x8a\xa1')]),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='item_id',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb9\xe7\x9b\xae\xe7\x9a\x84id'),
        ),
        migrations.AlterField(
            model_name='tb_goods',
            name='sp_id',
            field=models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x90\xe4\xbe\x9b\xe5\x95\x86'),
        ),
    ]
