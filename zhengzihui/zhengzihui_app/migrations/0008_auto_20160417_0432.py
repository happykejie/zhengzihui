# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0007_auto_20160417_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_accessory',
            name='anne_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='apubdate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_accessory',
            name='comm_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='affiliation_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='album_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='album_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='is_default',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='nacl_sort',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_album',
            name='upload_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='affiliation_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_click',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_sort',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='article_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='is_default',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_article',
            name='upload_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='album_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='pic_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tb_pic',
            name='upload_time',
            field=models.IntegerField(),
        ),
    ]
