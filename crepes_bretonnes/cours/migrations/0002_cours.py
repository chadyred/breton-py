# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=31)),
                ('eleves', models.ManyToManyField(to='cours.Eleve')),
            ],
        ),
    ]