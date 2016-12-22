# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161026_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='titre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorie',
            name='label',
            field=models.TextField(max_length=150),
        ),
    ]
