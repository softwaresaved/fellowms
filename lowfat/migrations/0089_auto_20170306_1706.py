# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0088_auto_20170301_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='grant_default',
            field=models.CharField(choices=[('SSI1', 'Software Sustainability Institute - Phase 1'), ('SSI2', 'Software Sustainability Institute - Phase 2'), ('SSI3', 'Software Sustainability Institute - Phase 3')], default='SS2', max_length=4),
        ),
        migrations.AddField(
            model_name='historicalfund',
            name='grant_default',
            field=models.CharField(choices=[('SSI1', 'Software Sustainability Institute - Phase 1'), ('SSI2', 'Software Sustainability Institute - Phase 2'), ('SSI3', 'Software Sustainability Institute - Phase 3')], default='SS2', max_length=4),
        ),
    ]
