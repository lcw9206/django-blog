# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-23 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20180419_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
