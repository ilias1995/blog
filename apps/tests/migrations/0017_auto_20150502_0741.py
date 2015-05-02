# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0016_auto_20150502_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 7, 41, 51, 138338)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 7, 41, 51, 139132)),
            preserve_default=True,
        ),
    ]
