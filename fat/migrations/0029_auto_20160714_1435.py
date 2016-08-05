# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fat', '0028_auto_20160713_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='budget_approve',
        ),
        migrations.AddField(
            model_name='event',
            name='budget_approved',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='amount_claimed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='fellow',
            name='application_year',
            field=models.IntegerField(default=2016),
        ),
        migrations.AddField(
            model_name='fellow',
            name='research_area_code',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fellow',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_attendance_fees',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_catering',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_others',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_subsistence_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_travel',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget_request_venue_hire',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='fellow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fat.Fellow'),
        ),
        migrations.AlterField(
            model_name='event',
            name='justification',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='expense',
            name='proof',
            field=models.FileField(blank=True, null=True, upload_to='expenses/'),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='phone',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='fellow',
            name='research_area',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='fellow',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='fellow',
            name='inauguration_year',
        ),
    ]
