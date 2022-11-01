from unittest.util import _MAX_LENGTH
from django.db import models

class aman(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    