# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0010_auto_20150610_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(max_length=1, null=True, choices=[('s', 'Student'), ('c', 'Company')]),
            preserve_default=True,
        ),
    ]
