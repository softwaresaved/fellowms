# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fat', '0021_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellow',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
