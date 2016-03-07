# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0022_remove_application_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_offer',
            field=models.CharField(default='bla', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='receiver',
            field=models.CharField(default='bla', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='sender',
            field=models.CharField(default='bla', max_length=70),
            preserve_default=False,
        ),
    ]
