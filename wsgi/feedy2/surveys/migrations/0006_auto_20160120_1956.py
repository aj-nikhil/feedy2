# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_auto_20160120_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyrecord',
            name='email_id',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Email'),
        ),
    ]
