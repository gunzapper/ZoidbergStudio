# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dicom_visio', '0003_dicom'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdatum',
            name='dicom',
            field=models.ForeignKey(default='', to='dicom_visio.Dicom'),
            preserve_default=True,
        ),
    ]
