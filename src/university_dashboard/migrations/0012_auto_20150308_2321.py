# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0011_auto_20150308_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 21, 24, 610572, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 21, 24, 609571, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
