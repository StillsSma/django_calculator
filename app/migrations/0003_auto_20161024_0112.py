# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_chirp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('u1', 'user1'), ('u2', 'user2')], max_length=1),
        ),
    ]
