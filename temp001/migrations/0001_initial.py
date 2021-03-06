# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-29 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp001.Teacher'),
        ),
    ]
