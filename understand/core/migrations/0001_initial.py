# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Preço')),
                ('slug', models.SlugField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('cep', models.CharField(max_length=8, verbose_name='Cep')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supermarket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supermarket', to='core.Supermarket'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='product', to='core.Product'),
        ),
    ]
