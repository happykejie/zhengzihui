# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fr_app', '0002_auto_20160730_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequireinfo',
            name='require_type',
            field=models.CharField(max_length=30, verbose_name=b'Require type', choices=[('\u9879\u76ee\u7533\u62a5', '\u9879\u76ee\u7533\u62a5'), ('\u5438\u5f15\u6295\u8d44', '\u5438\u5f15\u6295\u8d44'), ('\u4e89\u53d6\u8d37\u6b3e', '\u4e89\u53d6\u8d37\u6b3e'), ('\u5de5\u5546\u4ee3\u7406', '\u5de5\u5546\u4ee3\u7406'), ('\u8d44\u8d28\u4ee3\u529e', '\u8d44\u8d28\u4ee3\u529e'), ('\u77e5\u8bc6\u4ea7\u6743', '\u77e5\u8bc6\u4ea7\u6743'), ('\u8d22\u52a1\u670d\u52a1', '\u8d22\u52a1\u670d\u52a1'), (b'N1', b'N1')]),
        ),
    ]
