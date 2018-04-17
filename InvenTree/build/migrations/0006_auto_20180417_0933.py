# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 09:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0022_auto_20180417_0819'),
        ('build', '0005_buildoutput_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildoutput',
            name='build',
        ),
        migrations.RemoveField(
            model_name='buildoutput',
            name='part',
        ),
        migrations.AddField(
            model_name='build',
            name='batch',
            field=models.CharField(blank=True, help_text='Batch code for this build output', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='build',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='build',
            name='creation_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='build',
            name='notes',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='build',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='part.Part'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='build',
            name='quantity',
            field=models.PositiveIntegerField(default=1, help_text='Number of parts to build', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='build',
            name='title',
            field=models.CharField(default='Build title', help_text='Brief description of the build', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BuildOutput',
        ),
    ]
