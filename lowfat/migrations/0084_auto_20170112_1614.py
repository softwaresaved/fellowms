# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0083_auto_20161221_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimant',
            name='application_year',
            field=models.IntegerField(default=2017),
        ),
    ]
