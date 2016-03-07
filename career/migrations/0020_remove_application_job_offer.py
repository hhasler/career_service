# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0019_auto_20150616_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='job_offer',
        ),
    ]
