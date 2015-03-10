# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0010_auto_20150308_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 17, 55, 171753, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 9, 5, 17, 55, 170730, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
