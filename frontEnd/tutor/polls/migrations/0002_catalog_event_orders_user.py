# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_desc', models.CharField(max_length=100)),
                ('cat_pid', models.IntegerField(default=0)),
                ('cat_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=200)),
                ('e_time', models.DateTimeField(verbose_name='event')),
                ('e_date', models.CharField(default='Unknown', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_usrID', models.CharField(max_length=25)),
                ('order_desc', models.CharField(max_length=100)),
                ('order_pid', models.IntegerField(default=0)),
                ('order_wid', models.IntegerField(default=0)),
                ('order_quant', models.IntegerField(default=0)),
                ('order_status', models.IntegerField(default=0)),
                ('order_adrX', models.IntegerField(default=0)),
                ('order_adrY', models.IntegerField(default=0)),
                ('order_upsID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.CharField(default='null', max_length=200)),
                ('u_name', models.CharField(max_length=200)),
            ],
        ),
    ]
