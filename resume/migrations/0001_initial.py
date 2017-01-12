# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-17 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email_add', models.EmailField(max_length=80)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]