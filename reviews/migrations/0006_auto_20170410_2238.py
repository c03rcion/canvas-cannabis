# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20170410_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='height_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='strain',
            name='photo',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=reviews.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='strain',
            name='width_field',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
