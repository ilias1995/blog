# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20150429_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblock',
            name='litle',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
