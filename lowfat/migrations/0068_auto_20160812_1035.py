# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0067_auto_20160811_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='relative_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='draft_url',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tweet_url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='affiliation',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='funding',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='research_area',
            field=models.TextField(blank=True, help_text='Please describe your research'),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='website',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='website_feed',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='claimed',
            name='work_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='url',
            field=models.CharField(max_length=120),
        ),
    ]
