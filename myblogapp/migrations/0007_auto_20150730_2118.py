# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myblogapp', '0006_auto_20150730_1844'),
    ]

    operations = [
        migrations.RenameField(
                model_name='post',
                old_name='timestamp',
                new_name='pub_date',
        ),
    ]
