# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('Ads_id', models.AutoField(serialize=False, primary_key=True)),
                ('Content', models.CharField(max_length=1000)),
                ('Puton_Stuff', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('News_id', models.AutoField(serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=1000)),
                ('Content', models.TextField(max_length=10000)),
                ('Publish_Date', models.DateTimeField(verbose_name=b'date published')),
                ('Publish_Editer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.AutoField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Info', models.CharField(max_length=10000)),
                ('Price', models.IntegerField()),
                ('Puton_Stuff', models.CharField(max_length=100)),
            ],
        ),
    ]
