# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0016_auto_20160601_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellow',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
