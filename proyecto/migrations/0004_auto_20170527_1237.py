# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-27 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_proyecto_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]