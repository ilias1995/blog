# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_auto_20150501_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('blog', models.ForeignKey(to='tests.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blog',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 4, 44, 22, 340576)),
            preserve_default=True,
        ),
    ]
