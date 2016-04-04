# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myblogapp', '0003_auto_20150730_1830'),
    ]

    operations = [
        migrations.AlterField(
                model_name='post',
                name='mod_date',
                field=models.DateTimeField(default=None, null=True, verbose_name=b'date last modified'),
        ),
    ]
