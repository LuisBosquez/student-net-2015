# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0009_auto_20150308_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 15, 44, 175295, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 15, 44, 175295, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
    ]
