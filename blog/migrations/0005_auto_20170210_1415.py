# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170210_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='is_posted',
            new_name='is_visible',
        ),
        migrations.AddField(
            model_name='galery',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]
