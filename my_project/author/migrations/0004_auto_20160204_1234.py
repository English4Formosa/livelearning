# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_author_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=16),
        ),
    ]