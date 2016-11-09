# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20161103_2009'),
        ('class_room', '0005_class_requestuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_set', to='accounts.CustumUser')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='post',
            field=models.ManyToManyField(related_name='post_set', to='class_room.Post'),
        ),
    ]