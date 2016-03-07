# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0020_remove_application_job_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='receiver',
        ),
    ]
