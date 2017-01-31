# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0004_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft_url', models.CharField(max_length=120)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lowfat.Event')),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='proof',
            field=models.FileField(upload_to='expenses/'),
        ),
    ]
