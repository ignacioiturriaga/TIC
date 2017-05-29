# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-29 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='proyecto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='proyecto.proyecto'),
        ),
    ]
