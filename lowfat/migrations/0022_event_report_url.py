# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0021_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='report_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
