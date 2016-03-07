# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_auto_20150610_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(max_length=1, null=True, choices=[('1', 'Business Administration'), ('2', 'Architecture'), ('3', 'Entrepreneurship'), ('4', 'Finance'), ('5', 'Information Systems')]),
            preserve_default=True,
        ),
    ]
