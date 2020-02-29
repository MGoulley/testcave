# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class Parcelle(models.Model):
    numIlot = models.IntegerField(primary_key=True)
    nomParcelle = models.CharField(max_length=50)
    appellation = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50)
    surface = models.FloatField()

    class Meta:
        db_table = "parcelle"

    def __str__(self):
        return self.nomParcelle
