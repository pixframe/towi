# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-06 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0020_auto_20190202_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbolmusical',
            name='birds',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sombras',
            name='latencies',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]