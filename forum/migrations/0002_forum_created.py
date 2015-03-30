# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 22, 27, 34, 804719, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
