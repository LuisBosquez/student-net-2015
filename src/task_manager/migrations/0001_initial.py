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
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('dueDate', models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 15, 44, 178295, tzinfo=utc), verbose_name='Due Date')),
                ('dateCreated', models.DateTimeField(default=datetime.datetime(2015, 3, 9, 5, 15, 44, 178295, tzinfo=utc), verbose_name='Date Created')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('type', models.CharField(max_length=200, choices=[('WP', 'Work Plan'), ('UR', 'University Requirement'), ('IT', 'Internal Task')])),
                ('assignedTo', models.ManyToManyField(to='university_dashboard.Student')),
                ('studentGroup', models.ForeignKey(to='university_dashboard.StudentGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
