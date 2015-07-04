from django.db import models

class MDatum(models.Model):
    text = models.TextField(default='')
