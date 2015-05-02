# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_addblock_litle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblock',
            name='categori',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Categori',
        ),
    ]
