# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-04-21 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0034_auto_20190716_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arenamagicav2',
            name='change_level_clousure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arenamagicav2',
            name='change_level_motor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arenamagicav2',
            name='change_level_overlapping',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]