# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-29 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_comment_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='comment',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto'),
        ),
    ]