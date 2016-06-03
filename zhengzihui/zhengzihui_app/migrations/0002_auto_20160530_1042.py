# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhengzihui_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tb_accessory',
            options={'verbose_name': '\u5176\u4ed6\u9644\u4ef6\u8868', 'verbose_name_plural': '\u5176\u4ed6\u9644\u4ef6\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_album',
            options={'verbose_name': '\u76f8\u518c\u8868', 'verbose_name_plural': '\u76f8\u518c\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_apage',
            options={'verbose_name': '\u5355\u9875\u8868', 'verbose_name_plural': '\u5355\u9875\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_apage_class',
            options={'verbose_name': '\u5355\u9875\u5206\u7c7b\u8868', 'verbose_name_plural': '\u5355\u9875\u5206\u7c7b\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_area',
            options={'verbose_name': '\u5730\u533a\u8868', 'verbose_name_plural': '\u5730\u533a\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_article',
            options={'verbose_name': '\u6587\u7ae0\u8868', 'verbose_name_plural': '\u6587\u7ae0\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_artificial_representations',
            options={'verbose_name': '\u4eba\u5de5\u7533\u8ff0\u8868', 'verbose_name_plural': '\u4eba\u5de5\u7533\u8ff0\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_goods',
            options={'verbose_name': '\u670d\u52a1\u5546\u4fe1\u606f\u8868', 'verbose_name_plural': '\u670d\u52a1\u5546\u4fe1\u606f\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_goods_class',
            options={'verbose_name': '\u670d\u52a1\u5546\u5206\u7c7b\u8868', 'verbose_name_plural': '\u670d\u52a1\u5546\u5206\u7c7b\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_goods_click',
            options={'verbose_name': '\u670d\u52a1\u5546\u70b9\u51fb\u8868', 'verbose_name_plural': '\u670d\u52a1\u5546\u70b9\u51fb\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_goods_evaluation',
            options={'verbose_name': '\u670d\u52a1\u5546\u8bc4\u4ef7\u8868', 'verbose_name_plural': '\u670d\u52a1\u5546\u8bc4\u4ef7\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_item',
            options={'verbose_name': '\u9879\u76ee\u8be6\u60c5\u8868', 'verbose_name_plural': '\u9879\u76ee\u8be6\u60c5\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_item_class',
            options={'verbose_name': '\u9879\u76ee\u5206\u7c7b', 'verbose_name_plural': '\u9879\u76ee\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='tb_item_click',
            options={'verbose_name': '\u9879\u76ee\u70b9\u51fb\u8868', 'verbose_name_plural': '\u9879\u76ee\u70b9\u51fb\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_item_pa',
            options={'verbose_name': '\u9879\u76ee\u53d1\u5e03\u673a\u6784\u8868', 'verbose_name_plural': '\u9879\u76ee\u53d1\u5e03\u673a\u6784\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_message',
            options={'verbose_name': '\u7ad9\u5185\u77ed\u4fe1\u8868', 'verbose_name_plural': '\u7ad9\u5185\u77ed\u4fe1\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_messagetext',
            options={'verbose_name': '\u7ad9\u5185\u77ed\u4fe1\u5185\u5bb9\u8868', 'verbose_name_plural': '\u7ad9\u5185\u77ed\u4fe1\u5185\u5bb9\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_news',
            options={'verbose_name': '\u65b0\u95fb', 'verbose_name_plural': '\u65b0\u95fb'},
        ),
        migrations.AlterModelOptions(
            name='tb_news_class',
            options={'verbose_name': '\u65b0\u95fb\u7c7b\u522b', 'verbose_name_plural': '\u65b0\u95fb\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='tb_notice',
            options={'verbose_name': '\u516c\u544a ', 'verbose_name_plural': '\u516c\u544a'},
        ),
        migrations.AlterModelOptions(
            name='tb_notice_class',
            options={'verbose_name': '\u516c\u544a\u7c7b\u522b', 'verbose_name_plural': '\u516c\u544a\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='tb_order',
            options={'verbose_name': '\u8ba2\u5355\u8868', 'verbose_name_plural': '\u8ba2\u5355\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_pic',
            options={'verbose_name': '\u56fe\u7247\u8868', 'verbose_name_plural': '\u56fe\u7247\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_service_provider',
            options={'verbose_name': '\u670d\u52a1\u63d0\u4f9b\u5546', 'verbose_name_plural': '\u670d\u52a1\u63d0\u4f9b\u5546'},
        ),
        migrations.AlterModelOptions(
            name='tb_sysmessage',
            options={'verbose_name': '\u7cfb\u7edf\u4fe1\u606f\u8868', 'verbose_name_plural': '\u7cfb\u7edf\u4fe1\u606f\u8868'},
        ),
        migrations.AlterModelOptions(
            name='tb_user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='tb_user_expand',
            options={'verbose_name': '\u7528\u6237\u6269\u5c55\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u6269\u5c55\u4fe1\u606f'},
        ),
        migrations.RemoveField(
            model_name='tb_order',
            name='order_no',
        ),
        migrations.AddField(
            model_name='tb_order',
            name='goods_id',
            field=models.IntegerField(default=1980, verbose_name=b'\xe5\x95\x86\xe5\x93\x81id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tb_goods_evaluation',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe8\xaf\x84\xe4\xbb\xb7\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
