# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20150429_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='addblock',
            name='categori',
            field=models.ForeignKey(default=2, to='tests.Categori'),
            preserve_default=False,
        ),
    ]
