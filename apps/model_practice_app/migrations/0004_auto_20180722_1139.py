# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-22 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_practice_app', '0003_booker_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booker',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='books',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
