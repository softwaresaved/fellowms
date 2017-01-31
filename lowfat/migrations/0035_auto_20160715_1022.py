# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-15 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0034_expense_funds_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='asked_for_authorization_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='received_date',
            field=models.DateTimeField(default=datetime.date(2016, 7, 15)),
        ),
        migrations.AddField(
            model_name='expense',
            name='send_to_finance_date',
            field=models.DateTimeField(null=True),
        ),
    ]
