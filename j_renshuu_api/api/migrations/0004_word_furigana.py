# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171127_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='furigana',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
