# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-09 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170424_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='articlesTag',
        ),
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.Profile'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.Profile'),
        ),
        migrations.AlterField(
            model_name='usertagarticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.Profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
