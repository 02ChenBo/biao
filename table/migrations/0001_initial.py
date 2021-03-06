# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=15)),
                ('loc', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=15)),
                ('job', models.CharField(max_length=10)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateTimeField(auto_now=True)),
                ('sal', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('comm', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('deptno', models.IntegerField()),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
