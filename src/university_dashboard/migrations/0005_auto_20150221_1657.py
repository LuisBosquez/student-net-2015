# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0004_auto_20150221_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 57, 11, 816997, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French')], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 22, 57, 11, 816997, tzinfo=utc), verbose_name='date joined'),
            preserve_default=True,
        ),
    ]
