# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0005_auto_20150308_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 34, 1, 71010, tzinfo=utc), verbose_name='Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 34, 1, 71010, tzinfo=utc), verbose_name='Due Date'),
            preserve_default=True,
        ),
    ]
