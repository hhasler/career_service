# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0018_auto_20150611_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='company',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
