# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0072_auto_20160812_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='category_other',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
