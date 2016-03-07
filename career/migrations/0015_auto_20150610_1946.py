# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0014_userprofile_last_visited_jo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=70, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_visited_jo',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default=0, max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_dateOfBirth',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_degree',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[('B', 'BSc'), ('M', 'MSc')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_name',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_studyProgram',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[('B', 'Business Administration'), ('A', 'Architecture'), ('E', 'Entrepreneurship'), ('F', 'Finance'), ('I', 'Information Systems')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_surname',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
