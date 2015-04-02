# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='created',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
