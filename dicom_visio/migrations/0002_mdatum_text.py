# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dicom_visio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdatum',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
