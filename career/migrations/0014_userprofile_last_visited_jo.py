# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0013_auto_20150610_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_visited_jo',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
