# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0011_auto_20150610_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=500, null=True)),
                ('motivation_letter', models.FileField(upload_to=b'motivation_letter_pdf/')),
                ('job_offer', models.ForeignKey(to='career.JobOffer')),
                ('receiver', models.OneToOneField(related_name='receiver', to='career.UserProfile')),
                ('sender', models.OneToOneField(related_name='sender', to='career.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
