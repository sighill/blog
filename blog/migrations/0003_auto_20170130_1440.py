# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-30 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170130_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='img',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='is_posted',
            field=models.BooleanField(default=True),
        ),
    ]
