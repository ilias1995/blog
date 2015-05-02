# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0013_auto_20150501_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 18, 43, 24, 643621)),
            preserve_default=True,
        ),
    ]
