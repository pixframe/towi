# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-04 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0014_auto_20181004_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='arrange_spacialprecision_score',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]