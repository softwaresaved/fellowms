# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0050_auto_20160720_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='proof',
            new_name='claim',
        ),
    ]
