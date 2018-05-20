# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-03 02:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_auto_20170531_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='strain',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]