# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-06 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlddata', '0004_auto_20170628_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='hunger',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
