# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20170422_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo_number',
            field=models.BigIntegerField(null=True),
        ),
    ]