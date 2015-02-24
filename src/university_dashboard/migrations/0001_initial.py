# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('studentgroup_name', models.CharField(max_length=200)),
                ('studentgroup_size', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.AutoField(serialize=False, primary_key=True)),
                ('university_name', models.CharField(max_length=200)),
                ('university_location', models.CharField(max_length=200)),
                ('university_language', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='university_id',
            field=models.ForeignKey(to='university_dashboard.University'),
            preserve_default=True,
        ),
    ]
