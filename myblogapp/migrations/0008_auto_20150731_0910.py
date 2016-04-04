# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myblogapp', '0007_auto_20150730_2118'),
    ]

    operations = [
        migrations.CreateModel(
                name='Tag',
                fields=[
                    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('title', models.CharField(unique=True, max_length=100)),
                    ('slug', models.SlugField(unique=True, max_length=100)),
                ],
        ),
        migrations.AddField(
                model_name='post',
                name='slug',
                field=models.SlugField(default='tmp', unique=True, max_length=200),
                preserve_default=False,
        ),
        migrations.RemoveField(
                model_name='post',
                name='tags',
        ),
        migrations.AlterField(
                model_name='post',
                name='title',
                field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AddField(
                model_name='post',
                name='tags',
                field=models.ManyToManyField(to='myblogapp.Tag'),
        ),
    ]
