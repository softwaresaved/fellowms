# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0099_blog_coauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='notes_from_author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalblog',
            name='notes_from_author',
            field=models.TextField(blank=True, null=True),
        ),
    ]
