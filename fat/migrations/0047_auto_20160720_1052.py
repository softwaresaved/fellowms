# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fat', '0046_auto_20160720_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='proof',
            field=models.FileField(upload_to='expenses/'),
        ),
    ]
