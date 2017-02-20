# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-16 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170216_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='video',
            name='short_desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='video_tags', to='blog.Tag'),
        ),
    ]
