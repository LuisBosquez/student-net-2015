# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0008_auto_20150308_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 15, 12, 266836, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 15, 12, 265835, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
