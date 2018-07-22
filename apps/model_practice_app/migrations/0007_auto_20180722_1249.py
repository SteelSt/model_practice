# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-22 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_practice_app', '0006_dojo_ninja'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='model_practice_app.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]