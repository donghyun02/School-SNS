# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20161119_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumuser',
            name='profileImage',
            field=models.ImageField(default='./static/profiles/default.jpg', upload_to='./static/profiles/'),
        ),
    ]