# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0015_auto_20150502_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 5, 32, 56, 761934)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 5, 32, 56, 761241)),
            preserve_default=True,
        ),
    ]
