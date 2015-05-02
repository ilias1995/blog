# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_auto_20150429_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.TextField()),
                ('addcomputer', models.ForeignKey(to='tests.Addcomputers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.TextField()),
                ('addnetwork', models.ForeignKey(to='tests.Addnetwork')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.TextField()),
                ('addprograming', models.ForeignKey(to='tests.Addprograming')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
