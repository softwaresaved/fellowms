# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fat', '0062_auto_20160809_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Fund',
        ),
    ]