# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('zhengzihui_app', '0003_auto_20160403_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('back', filer.fields.image.FilerImageField(related_name='book_backs', blank=True, to='filer.Image', null=True)),
                ('content', filer.fields.file.FilerFileField(related_name='company_disclaimer', blank=True, to='filer.File', null=True)),
                ('cover', filer.fields.image.FilerImageField(related_name='book_covers', blank=True, to='filer.Image', null=True)),
            ],
        ),
    ]
