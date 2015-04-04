# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150403_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='thumbnail1',
            field=models.ImageField(null=True, upload_to='profile_images/thumbs/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='thumbnail2',
            field=models.ImageField(null=True, upload_to='profile_images/thumbs/', blank=True),
            preserve_default=True,
        ),
    ]
