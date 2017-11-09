# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalRanking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('measure_id', models.CharField(blank=True, max_length=255, null=True)),
                ('measure_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Measure_info',
                'managed': False,
            },
        ),
    ]