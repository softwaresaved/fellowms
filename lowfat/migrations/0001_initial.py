# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('url', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('budget_request', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fellow',
            fields=[
                ('email', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=120, unique=True)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='fellow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lowfat.Fellow'),
        ),
    ]
