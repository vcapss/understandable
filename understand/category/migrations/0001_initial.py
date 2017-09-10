# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-10 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='product', to='products.Product')),
            ],
        ),
    ]
