# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0007_auto_20150308_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 10, 14, 699810, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 10, 14, 698810, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
    ]
