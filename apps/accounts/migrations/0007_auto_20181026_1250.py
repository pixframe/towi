# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181025_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'Escuela'},
        ),
        migrations.RemoveField(
            model_name='children',
            name='active',
        ),
        migrations.RemoveField(
            model_name='children',
            name='trial_active',
        ),
    ]
