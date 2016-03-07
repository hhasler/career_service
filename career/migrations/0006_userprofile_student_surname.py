# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0005_auto_20150610_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_surname',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
    ]
