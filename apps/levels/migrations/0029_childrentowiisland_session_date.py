# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-09 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0028_average_quartile'),
    ]

    operations = [
        migrations.AddField(
            model_name='childrentowiisland',
            name='session_date',
            field=models.DateField(default='2019-05-08'),
            preserve_default=False,
        ),
    ]
