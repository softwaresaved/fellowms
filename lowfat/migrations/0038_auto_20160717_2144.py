# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0037_auto_20160715_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='website',
            field=models.URLField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='website_feed',
            field=models.URLField(blank=True, max_length=120),
        ),
    ]
