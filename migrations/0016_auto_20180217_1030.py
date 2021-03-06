# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-17 05:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0015_auto_20170601_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='foodlist',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='foodqty',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
