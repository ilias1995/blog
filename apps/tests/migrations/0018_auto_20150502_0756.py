# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0017_auto_20150502_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 7, 56, 27, 814713)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 7, 56, 27, 815392)),
            preserve_default=True,
        ),
    ]
