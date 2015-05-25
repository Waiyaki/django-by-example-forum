# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
