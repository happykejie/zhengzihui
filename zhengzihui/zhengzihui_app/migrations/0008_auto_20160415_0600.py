# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0007_auto_20160415_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_notice',
            name='Article_id',
            field=models.IntegerField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0ID'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Nocl_id',
            field=models.IntegerField(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbID'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_is_display',
            field=models.IntegerField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_sort',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_source',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\x9d\xa5\xe6\xba\x90'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_time',
            field=models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_title',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='tb_notice',
            name='Notice_top',
            field=models.IntegerField(verbose_name=b'\xe5\xbc\xba\xe5\x88\xb6\xe7\xbd\xae\xe9\xa1\xb6'),
        ),
    ]
