# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]