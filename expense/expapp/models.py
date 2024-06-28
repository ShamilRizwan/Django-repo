from django import forms
from django.db import models

# Create your models here.
class ExpenseT(models.Model):
    expname=models.CharField(max_length=20)
    expense=models.IntegerField(20)

    def __str__(self):
        return self.expname

class Balance(models.Model):
    balamt=models.IntegerField(20)