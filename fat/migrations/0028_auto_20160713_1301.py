# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-13 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fat', '0027_auto_20160713_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellow',
            name='fellowship_grant',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
