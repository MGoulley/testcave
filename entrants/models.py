# -*- encoding: utf-8 -*-
from django.db import models
from administration.models import Domaine
from administration.models import Organisation

class Parcelle(models.Model):
    numIlot = models.IntegerField()
    nomParcelle = models.CharField(max_length=50)
    domaines = models.ManyToManyField(Domaine, through='ParcelleEtendue')
    appellation = models.CharField(max_length=50)       
    commune = models.CharField(max_length=50)
    refCadastre = models.CharField(max_length=50)
    anneesPlantation = models.CharField(max_length=50)
    datebio = models.IntegerField()

    class Meta:
        db_table = "parcelles"

    def __str__(self):
        return self.nomParcelle

class Materiels(models.Model):
    nom = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    class Meta:
        db_table = "materiels"

class ParcelleEtendue(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    proprietaire = models.CharField(primary_key=True,max_length=50)
    surface = models.FloatField()

    class Meta:
        db_table = "parcelle-domaines"

