# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_cours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surveillant',
            fields=[
                ('eleve_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cours.Eleve')),
                ('rang', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('cours.eleve',),
        ),
        migrations.RemoveField(
            model_name='cours',
            name='eleves',
        ),
        migrations.AddField(
            model_name='eleve',
            name='prenom',
            field=models.CharField(default=1, max_length=31),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eleve',
            name='sexe',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.CreateModel(
            name='SurveillantProxy',
            fields=[
            ],
            options={
                'ordering': ['rang'],
                'proxy': True,
            },
            bases=('cours.surveillant',),
        ),
    ]
