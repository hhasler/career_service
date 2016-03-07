# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0012_auto_20150610_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='student_degree',
            field=models.CharField(max_length=1, null=True, choices=[('B', 'BSc'), ('M', 'MSc')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_studyProgram',
            field=models.CharField(max_length=1, null=True, choices=[('B', 'Business Administration'), ('A', 'Architecture'), ('E', 'Entrepreneurship'), ('F', 'Finance'), ('I', 'Information Systems')]),
            preserve_default=True,
        ),
    ]
