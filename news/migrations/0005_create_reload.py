# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 20:07
from __future__ import unicode_literals

from django.db import migrations, models


def create_reload(apps, schema_editor):
    Reload = apps.get_registered_model('news', 'Reload')
    reloads = Reload(reloads=False)
    reloads.save()


class Migration(migrations.Migration):

     dependencies = [
         ('news', '0004_reload')
     ]

     operations = [
         migrations.RunPython(create_reload),
     ]
