# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20141118_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hobbies',
            field=models.TextField(default=datetime.datetime(2014, 11, 18, 20, 50, 5, 806759, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='line_of_work',
            field=models.CharField(default=datetime.datetime(2014, 11, 18, 20, 50, 54, 478790, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='self_description',
            field=models.TextField(default=datetime.datetime(2014, 11, 18, 20, 51, 4, 201799, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vehicle_model',
            field=models.CharField(default=datetime.datetime(2014, 11, 18, 20, 51, 15, 73738, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
