# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-08 21:41
from __future__ import unicode_literals

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=20)),
                ('relation', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, default='/avatars/default_user.png', upload_to='avatars')),
                ('dob', models.DateField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('register_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('vcode', models.CharField(max_length=500)),
                ('link_id', models.CharField(max_length=10)),
                ('fb_id', models.CharField(blank=True, max_length=200)),
                ('user_type', models.CharField(choices=[('especialista', 'Especialista'), ('familiar', 'Familiar'), ('escuela', 'Escuela'), ('investigador', 'Investigador')], default='familiar', max_length=50)),
                ('account_type', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('specialty', models.CharField(blank=True, max_length=100)),
                ('greeting', models.CharField(blank=True, max_length=100)),
                ('researcher', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Es staff')),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='center')),
            ],
            options={
                'verbose_name': 'Centro',
            },
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('laterality', models.CharField(choices=[('derecho', 'Derecho'), ('zurdo', 'Zurdo'), ('desconocido', 'desconocido')], default='desconocido', max_length=100)),
                ('videogames_usage', models.FloatField(blank=True, null=True)),
                ('learning_disabilities', models.CharField(blank=True, max_length=300)),
                ('failed_grades', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, choices=[('Kinder', 'Kinder'), ('Preprimaria', 'Preprimaria'), ('1 primaria', '1º Primaria'), ('2 primaria', '2º Primaria'), ('3 primaria', '3º Primaria'), ('4 primaria', '4º Primaria'), ('5 primaria', '5º Primaria'), ('6 primaria', '6º Primaria')], max_length=100)),
                ('genre', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=100)),
                ('school_name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('picture', models.ImageField(blank=True, default='/avatars/default_user.png', upload_to='avatars')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('trial_active', models.BooleanField(default=False)),
                ('diagnostic', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=50)),
            ],
            options={
                'verbose_name': 'Niño',
                'verbose_name_plural': 'Niños',
            },
        ),
        migrations.CreateModel(
            name='FreeTrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md5_device', models.CharField(max_length=100)),
                ('trial_id', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Free Trial',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('children', models.ManyToManyField(blank=True, to='accounts.Children')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='LinkedAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_u1', models.BooleanField(default=False)),
                ('auth_u2', models.BooleanField(default=False)),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_linked_account', to=settings.AUTH_USER_MODEL)),
                ('shared_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_linked_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cuentas Ligadas',
            },
        ),
        migrations.CreateModel(
            name='LinkedAccountsOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.BooleanField(default=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='accounts.Children')),
                ('linked_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='accounts.LinkedAccounts')),
            ],
            options={
                'verbose_name_plural': 'Option de Cuentas Ligadas',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(blank=True, choices=[('public', 'PUblic'), ('private', 'Private')], max_length=50)),
                ('regular_special', models.CharField(blank=True, choices=[('regular', 'Regular'), ('special', 'Special')], max_length=100)),
                ('mixed_differetiated', models.CharField(blank=True, choices=[('mixed', 'Mixed'), ('men', 'Men'), ('Woman', 'Woman')], max_length=100)),
                ('city', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo usuario',
            },
        ),
        migrations.AddField(
            model_name='children',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.School'),
        ),
        migrations.AddField(
            model_name='children',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='center',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Center'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.School'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]