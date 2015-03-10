# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university_dashboard', '0006_auto_20150303_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assignedTo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='studentGroup',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(upload_to='thumbpath', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 9, 29, 449968, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 9, 29, 448967, tzinfo=utc), verbose_name='Date Joined'),
            preserve_default=True,
        ),
    ]
