# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_create_reload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reload',
        ),
    ]
