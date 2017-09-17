# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-10 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Preço')),
                ('slug', models.SlugField(editable=False, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('supermarket', models.ManyToManyField(related_name='supermarket', to='supermarket.Supermarket')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]