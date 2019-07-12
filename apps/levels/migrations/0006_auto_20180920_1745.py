# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-20 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0005_auto_20180919_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childrentowiisland',
            name='arbol_first_time',
        ),
        migrations.AlterField(
            model_name='childrentowiisland',
            name='arena_first_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='childrentowiisland',
            name='bolita_first_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='childrentowiisland',
            name='rio_first_time',
            field=models.BooleanField(db_column='rioTutorial', default=True),
        ),
        migrations.AlterField(
            model_name='childrentowiisland',
            name='sombras_first_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='childrentowiisland',
            name='tesoro_first_time',
            field=models.BooleanField(db_column='arbolMusicalTutorial', default=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='sessions', to='accounts.Children'),
        ),
    ]
