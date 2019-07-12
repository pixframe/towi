# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-08 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('max_kids', models.IntegerField()),
                ('ammount', models.FloatField(default=0.0)),
                ('recurrency', models.CharField(max_length=50)),
                ('promo_code', models.CharField(blank=True, max_length=200)),
                ('user_id', models.IntegerField()),
                ('user_email', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('open_pay_id', models.CharField(blank=True, max_length=200, null=True)),
                ('open_pay_order_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
        migrations.CreateModel(
            name='Promos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('unique', models.BooleanField(default=False)),
                ('promo_code', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Promocion',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_kids', models.IntegerField()),
                ('key', models.CharField(blank=True, max_length=240, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='suscription', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Suscripcion',
                'verbose_name_plural': 'Suscripciones',
            },
        ),
        migrations.CreateModel(
            name='SuscriptionChildren',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('finished_date', models.DateTimeField(verbose_name='Fecha fin')),
                ('is_suscription', models.BooleanField(default=False)),
                ('trial', models.BooleanField(default=False)),
                ('order', models.CharField(blank=True, max_length=200, null=True)),
                ('children', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suscription', to='accounts.Children')),
                ('suscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='suscriptions.Suscription')),
            ],
            options={
                'verbose_name': 'Suscription Date',
            },
        ),
        migrations.CreateModel(
            name='SuscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(choices=[('unsuscribe', 'Sin suscripción'), ('monthly', 'Mensual'), ('quarterly', 'Trimestral')], default='unsuscribe', max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Tipo suscripcion',
                'verbose_name_plural': 'Tipo de suscripciones',
            },
        ),
        migrations.AddField(
            model_name='suscriptionchildren',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suscriptions.SuscriptionType'),
        ),
        migrations.AddField(
            model_name='promos',
            name='suscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promos', to='suscriptions.SuscriptionType'),
        ),
    ]
