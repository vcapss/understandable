# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170908_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
