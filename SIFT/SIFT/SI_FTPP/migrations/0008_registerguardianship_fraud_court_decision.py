# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SI_FTPP', '0007_auto_20161219_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerguardianship',
            name='fraud_court_decision',
            field=models.BooleanField(default=False, verbose_name='Fraude a resoluci\xf3n judicial'),
        ),
    ]
