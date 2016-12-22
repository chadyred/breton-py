# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161026_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('libelle', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserTagArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='usertagarticle',
            name='article',
            field=models.ForeignKey(to='blog.Article'),
        ),
        migrations.AddField(
            model_name='usertagarticle',
            name='tag',
            field=models.ForeignKey(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='usertagarticle',
            name='user',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='articleTag',
            field=models.ManyToManyField(to='blog.Article', through='blog.UserTagArticle', related_name='user_tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(to='blog.Article', through='blog.UserTagArticle'),
        ),
    ]
