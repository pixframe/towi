# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0008_auto_20180928_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='coinspatterntype',
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='packtimeofcomp',
        ),
    ]
