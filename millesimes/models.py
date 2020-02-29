# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class Millesime(models.Model):
    annee = models.IntegerField(primary_key=True)
    nomMillesime = models.CharField(max_length=20)

    class Meta:
        db_table = "millesime"
