# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-14 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlddata', '0005_foods_hunger'),
    ]

    operations = [
        migrations.CreateModel(
            name='character_attributes_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, unique=True)),
                ('key', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Character Attrubute Information',
                'verbose_name_plural': 'Character Attribute Information',
            },
        ),
        migrations.CreateModel(
            name='equipment_attributes_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, unique=True)),
                ('key', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Equipment Attrubute Information',
                'verbose_name_plural': 'Equipment Attribute Information',
            },
        ),
        migrations.CreateModel(
            name='food_attributes_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, unique=True)),
                ('key', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Food Attrubute Information',
                'verbose_name_plural': 'Food Attribute Information',
            },
        ),
        migrations.RemoveField(
            model_name='character_models',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='character_models',
            name='defence',
        ),
        migrations.RemoveField(
            model_name='character_models',
            name='max_mp',
        ),
        migrations.RemoveField(
            model_name='equipments',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='equipments',
            name='defence',
        ),
        migrations.RemoveField(
            model_name='foods',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='foods',
            name='hunger',
        ),
        migrations.RemoveField(
            model_name='foods',
            name='mp',
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_10',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_3',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_4',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_5',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_6',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_7',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_8',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='character_models',
            name='attr_9',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_10',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_3',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_4',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_5',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_6',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_7',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_8',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='equipments',
            name='attr_9',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_10',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_3',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_4',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_5',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_6',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_7',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_8',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='foods',
            name='attr_9',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
