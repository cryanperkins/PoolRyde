# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signup',
            name='last_name',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
