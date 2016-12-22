# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161027_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='articleTag',
            new_name='articlesTag',
        ),
    ]
