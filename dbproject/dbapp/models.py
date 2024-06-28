from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name