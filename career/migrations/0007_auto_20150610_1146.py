# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_userprofile_student_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_dateOfBirth',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='student_name',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
    ]
