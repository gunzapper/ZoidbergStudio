from django.db import models

class Dicom(models.Model):
    pass

class MDatum(models.Model):
    text = models.TextField(default='')
    dicom = models.ForeignKey(Dicom, default='')

