# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShelfLife', '0003_remove_thing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(default='https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj72KvMlcLVAhUKsI8KHTRSAp8QjRwIBw&url=http%3A%2F%2Fdeathbattlefanon.wikia.com%2Fwiki%2FSlappy_the_Dummy&psig=AFQjCNE0KK5qOa87zSc5eI3Yb8sfGQ9eLw&ust=1502093795923614', max_length=1000),
        ),
    ]
