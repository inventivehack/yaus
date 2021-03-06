# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('url', models.CharField(blank=True, max_length=900, unique=True)),
                ('redirect_url', models.URLField()),
                ('hits', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
    ]
