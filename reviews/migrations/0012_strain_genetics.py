# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 20:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20170422_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='genetics',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]