# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-13 09:24
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180413_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=100, verbose_name='자기소개'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=accounts.models.set_profile_path, verbose_name='프로필 사진'),
        ),
    ]
