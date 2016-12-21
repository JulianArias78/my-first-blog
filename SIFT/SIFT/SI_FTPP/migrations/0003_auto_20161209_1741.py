# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SI_FTPP', '0002_auto_20161123_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerguardianship',
            name='adult_greater',
        ),
        migrations.RemoveField(
            model_name='registerguardianship',
            name='legal_guardian',
        ),
        migrations.RemoveField(
            model_name='registerguardianship',
            name='ownName',
        ),
        migrations.RemoveField(
            model_name='registerguardianship',
            name='unofficial_agent',
        ),
        migrations.RemoveField(
            model_name='registerguardianship',
            name='younger',
        ),
        migrations.AddField(
            model_name='registerguardianship',
            name='in_respresentation',
            field=models.CharField(choices=[('1', 'Adulto Mayor'), ('2', 'Menor de edad'), ('3', 'En Nombre Propio'), ('4', 'Mediante Apoderado'), ('5', 'Agente Oficioso')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'LGTBI')], default='M', max_length=10, verbose_name='G\xe9nero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('A', 'Administrador'), ('AUX', 'Auxiliar'), ('END', 'Consultor')], max_length=1, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='condition',
            field=models.CharField(choices=[('1', 'V\xedctima'), ('2', 'Discapacidad'), ('3', 'Menor'), ('4 Mayor', 'Adulto Mayor')], default='1', max_length=25, verbose_name='Condici\xf3n'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='ethnic_group',
            field=models.CharField(choices=[('1', 'Mestizo - Blanco'), ('2', 'Afro'), ('3', 'Rom'), ('4', 'Indigena')], default='1', max_length=25, verbose_name='Etnia'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'LGTBI')], default='M', max_length=10, verbose_name='G\xe9nero'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='improper_for',
            field=models.CharField(choices=[('1', 'Hecho superado'), ('2', 'Da\xf1o consumado'), ('3', 'Existe otro medio de defensa'), ('4', 'Otro')], default='1', max_length=25, verbose_name='Improcedente'),
        ),
        migrations.AlterField(
            model_name='registerguardianship',
            name='regime',
            field=models.CharField(choices=[('1', 'Subsidiado'), ('2', 'Contributivo')], default='1', max_length=15, verbose_name='R\xe9gimen'),
        ),
    ]