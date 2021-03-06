# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-10 03:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fist_name', models.CharField(blank=True, max_length=100)),
                ('apellido1', models.CharField(blank=True, max_length=80)),
                ('apellido2', models.CharField(blank=True, max_length=80)),
                ('rut', models.CharField(blank=True, max_length=9)),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('colegio', models.CharField(blank=True, max_length=200)),
                ('curso', models.IntegerField(blank=True)),
                ('foto', models.ImageField(blank=True, upload_to='estudiantes')),
                ('tipo_usuario', models.CharField(choices=[('ESTUDIANTE', 'Estudiante'), ('COLABORADOR', 'Colaborador')], max_length=10)),
            ],
        ),
    ]
