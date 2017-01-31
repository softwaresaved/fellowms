# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0003_auto_20160413_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('P', 'Processing'), ('F', 'Finished')], default='P', max_length=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lowfat.Event')),
            ],
        ),
    ]
