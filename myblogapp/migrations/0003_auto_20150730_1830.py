# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0002_auto_20150730_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mod_date',
            field=models.DateTimeField(default=None, verbose_name=b'date last modified'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
