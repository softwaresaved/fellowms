# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 15:59
from __future__ import unicode_literals

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0012_auto_20160429_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
