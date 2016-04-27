# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0011_auto_20160424_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_service_provider',
            name='sp_image1',
            field=models.ImageField(upload_to=b'img/tb_service_provider_sp_img1/%Y/%m/%d', verbose_name=b'\xe6\x94\xbf\xe8\xb5\x84\xe6\xb1\x87\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe8\xaf\x81\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0'),
        ),
        migrations.AlterField(
            model_name='tb_service_provider',
            name='sp_image2',
            field=models.ImageField(upload_to=b'img/tb_service_provider_sp_img2/%Y/%m/%d', verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe6\x89\x80\xe4\xbb\xa3\xe8\xa1\xa8\xe7\x9a\x84\xe5\x85\xac\xe5\x8f\xb8\xe6\x89\xa7\xe7\x85\xa7\xe4\xb8\x8a\xe4\xbc\xa0'),
        ),
    ]
