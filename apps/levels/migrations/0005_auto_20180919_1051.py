# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-19 15:51
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0004_session_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='games',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ArbolMusical', 'ArbolMusical'), ('Rio', 'Rio'), ('ArenaMagica', 'ArenaMagica'), ('DondeQuedoLaBolita', 'DondeQuedoLaBolita'), ('Tesoro', 'Tesoro'), ('JuegoDeSombras', 'JuegoDeSombras')], max_length=69),
        ),
    ]
