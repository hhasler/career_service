# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0009_userprofile_student_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='student_degree',
            field=models.CharField(max_length=1, null=True, choices=[('BSc', 'BSc'), ('MSc', 'MSc')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_studyProgram',
            field=models.CharField(max_length=1, null=True, choices=[('BA', 'Business Administration'), ('A', 'Architecture'), ('E', 'Entrepreneurship'), ('F', 'Finance'), ('IS', 'Information Systems')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(max_length=1, null=True, choices=[('student', 'Student'), ('company', 'Company')]),
            preserve_default=True,
        ),
    ]
