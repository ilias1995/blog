# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_auto_20150501_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 16, 53, 41, 528967)),
            preserve_default=True,
        ),
    ]
