# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='university_language',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
    ]
