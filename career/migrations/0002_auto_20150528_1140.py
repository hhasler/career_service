# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('company', models.CharField(max_length=70)),
                ('position', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('workloadPercentage', models.IntegerField(default=100)),
                ('expectations', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
                ('pdf_file', models.FileField(upload_to=b'job_offer_pdf/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=70)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('is_student', models.BooleanField(default=True)),
                ('is_corporate', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
