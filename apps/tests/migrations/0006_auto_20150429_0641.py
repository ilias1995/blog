# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_auto_20150429_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblock',
            name='categori',
            field=models.CharField(max_length=2, choices=[(b'TS', b'Toshibo'), (b'SM', b'Samsung'), (b'MB', b'MacBokk')]),
            preserve_default=True,
        ),
    ]
