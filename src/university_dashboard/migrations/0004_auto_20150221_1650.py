# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0003_auto_20150221_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 50, 36, 172450, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 50, 36, 172450, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
    ]
