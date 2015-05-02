# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_auto_20150429_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcomputers',
            old_name='date_job',
            new_name='date_block',
        ),
        migrations.RenameField(
            model_name='addnetwork',
            old_name='date_job',
            new_name='date_block',
        ),
        migrations.RemoveField(
            model_name='addprograming',
            name='date_job',
        ),
        migrations.AddField(
            model_name='addprograming',
            name='date_block',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
