# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-25 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion_imagen', models.CharField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/Galeria/')),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/Logos/')),
                ('descripcion_general', models.TextField(blank=True, max_length=200)),
                ('descripcion_detallada', models.TextField(blank=True, max_length=1500)),
                ('definicion_problema', models.TextField(blank=True, max_length=1500)),
                ('definicion_solucion', models.TextField(blank=True, max_length=1500)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('galeria_imagenes', models.ManyToManyField(blank=True, to='proyecto.Galeria')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]