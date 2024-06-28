from django import forms
from django.db import models

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField(20)

    def __str__(self):
        return self.name