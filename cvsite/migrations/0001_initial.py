# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
