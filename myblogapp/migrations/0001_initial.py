# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name='Post',
                fields=[
                    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('body', models.TextField()),
                    ('title', models.CharField(max_length=500)),
                    ('timestamp', models.CharField(max_length=50)),
                    ('tags', models.CharField(max_length=200)),
                ],
        ),
    ]
