# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fat', '0049_auto_20160720_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='asked_for_authorization_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='send_to_finance_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
