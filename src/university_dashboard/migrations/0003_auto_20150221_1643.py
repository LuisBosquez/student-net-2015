# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0002_auto_20150221_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentgroup',
            old_name='studentgroup_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studentgroup',
            old_name='studentgroup_size',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='university',
            name='university_id',
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='category',
            field=models.CharField(default='None specified', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 43, 21, 338789, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='university',
            name='id',
            field=models.AutoField(default=0, primary_key=True, verbose_name='ID', serialize=False, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 43, 21, 338789, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
    ]
