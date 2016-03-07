# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20150528_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_corporate',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_student',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default=0, max_length=12),
            preserve_default=True,
        ),
    ]
