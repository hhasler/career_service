# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0008_userprofile_student_studyprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_degree',
            field=models.CharField(max_length=1, null=True, choices=[('1', 'BSc'), ('2', 'MSc')]),
            preserve_default=True,
        ),
    ]
