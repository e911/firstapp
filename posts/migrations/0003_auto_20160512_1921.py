# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160512_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dept',
            field=models.CharField(default=datetime.datetime(2016, 5, 12, 19, 21, 7, 221168, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.CharField(default=datetime.datetime(2016, 5, 12, 19, 21, 13, 645856, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
