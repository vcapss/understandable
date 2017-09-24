# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-24 17:27
from __future__ import unicode_literals

import brazilnum.cnpj
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_reason', models.CharField(max_length=100)),
                ('cnpj', models.CharField(blank=True, max_length=12, validators=[brazilnum.cnpj.validate_cnpj])),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('cep', models.CharField(max_length=8, verbose_name='Cep')),
            ],
        ),
    ]
