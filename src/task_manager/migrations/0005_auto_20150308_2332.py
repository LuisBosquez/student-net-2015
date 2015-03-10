# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_auto_20150308_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateCreated',
            field=models.DateTimeField(verbose_name='Date Created', default=datetime.datetime(2015, 3, 9, 5, 32, 37, 32129, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(verbose_name='Due Date', default=datetime.datetime(2015, 3, 9, 5, 32, 37, 32129, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
