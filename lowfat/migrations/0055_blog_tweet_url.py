# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-04 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0054_auto_20160804_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tweet_url',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
    ]
