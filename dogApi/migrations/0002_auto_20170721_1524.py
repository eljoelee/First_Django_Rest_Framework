# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dogPersonality',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='dogPob',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]