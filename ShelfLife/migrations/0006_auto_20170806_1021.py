# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfLife', '0005_auto_20170806_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='desc',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
