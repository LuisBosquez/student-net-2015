# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0012_auto_20150308_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 32, 33, 860243, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 32, 33, 860243, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
    ]
