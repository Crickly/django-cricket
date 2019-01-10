# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0004_auto_20181218_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='pc_slug',
        ),
        migrations.AddField(
            model_name='club',
            name='home_club',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]