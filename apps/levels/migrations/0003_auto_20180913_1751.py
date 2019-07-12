# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-13 22:51
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_auto_20180913_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='games',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ArbolMusical', 'Arbol Musical'), ('Rio', 'Rio'), ('ArenaMagica', 'Arena Magica'), ('DondeQuedoLaBolita', 'Donde Quedo La Bolita'), ('Tesoro', 'Tesoro'), ('JuegoDeSombras', 'Juego De Sombras')], max_length=69),
        ),
    ]