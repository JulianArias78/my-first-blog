# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SI_FTPP', '0006_remove_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerguardianship',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='condition',
            field=models.CharField(choices=[('1', 'V\xedctima'), ('2', 'Discapacidad'), ('3', 'Menor'), ('4', 'Adulto Mayor'), ('5', 'Habitante de calle')], default='1', max_length=25, verbose_name='Condici\xf3n'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='which_entity',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cu\xe1l Entidad?'),
        ),
    ]
