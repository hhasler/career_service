# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0017_auto_20150610_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='company',
            field=models.ForeignKey(to='career.UserProfile'),
            preserve_default=True,
        ),
    ]
