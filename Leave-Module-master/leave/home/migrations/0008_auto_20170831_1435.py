# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170831_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]