# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='num1',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='num2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
