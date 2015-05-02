# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0011_compcomments_netcomments_progcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_name', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2015, 5, 1, 16, 52, 59, 580817))),
                ('blog_text', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='addcomputers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='addnetwork',
            name='user',
        ),
        migrations.RemoveField(
            model_name='addprograming',
            name='user',
        ),
        migrations.RemoveField(
            model_name='compcomments',
            name='addcomputer',
        ),
        migrations.DeleteModel(
            name='Addcomputers',
        ),
        migrations.DeleteModel(
            name='CompComments',
        ),
        migrations.RemoveField(
            model_name='netcomments',
            name='addnetwork',
        ),
        migrations.DeleteModel(
            name='Addnetwork',
        ),
        migrations.DeleteModel(
            name='NetComments',
        ),
        migrations.RemoveField(
            model_name='progcomments',
            name='addprograming',
        ),
        migrations.DeleteModel(
            name='Addprograming',
        ),
        migrations.DeleteModel(
            name='ProgComments',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(to='tests.BlogType'),
            preserve_default=True,
        ),
    ]
