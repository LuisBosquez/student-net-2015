# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0005_auto_20150221_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, default='Some student')),
                ('email', models.CharField(max_length=200, default='email@university.edu')),
                ('major', models.CharField(max_length=200, choices=[('CS', 'Computer Science'), ('EC', 'Economics'), ('FI', 'Finance'), ('MK', 'Marketing')])),
                ('studentGroup', models.ForeignKey(to='university_dashboard.StudentGroup')),
                ('university', models.ForeignKey(to='university_dashboard.University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('dueDate', models.DateTimeField(verbose_name='Due Date', default=datetime.datetime(2015, 3, 4, 5, 45, 13, 920048, tzinfo=utc))),
                ('dateCreated', models.DateTimeField(verbose_name='Date Created', default=datetime.datetime(2015, 3, 4, 5, 45, 13, 920048, tzinfo=utc))),
                ('status', models.BooleanField(verbose_name='Status', default=False)),
                ('type', models.CharField(max_length=200, choices=[('WP', 'Work Plan'), ('UR', 'University Requirement'), ('IT', 'Internal Task')])),
                ('assignedTo', models.ManyToManyField(to='university_dashboard.Student')),
                ('studentGroup', models.ForeignKey(to='university_dashboard.StudentGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='studentgroup',
            old_name='university_id',
            new_name='university',
        ),
        migrations.RemoveField(
            model_name='studentgroup',
            name='size',
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='description',
            field=models.TextField(verbose_name='Description', default='Some student group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='category',
            field=models.CharField(max_length=200, default='None specified', choices=[('MJ', 'Major'), ('RA', 'Recreational Activty'), ('MS', 'Miscellaneous')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 4, 5, 45, 13, 920048, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(max_length=200, default='Some student group name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='memberSince',
            field=models.DateTimeField(verbose_name='Date Joined', default=datetime.datetime(2015, 3, 4, 5, 45, 13, 920048, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=200, default='Some university'),
            preserve_default=True,
        ),
    ]
