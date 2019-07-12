# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-01 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0012_header_application_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='weather_coherence',
        ),
        migrations.AddField(
            model_name='prueba',
            name='weather_time',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
