# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-29 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_goodstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('spec', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='static/upload/goods')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
