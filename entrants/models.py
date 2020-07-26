# -*- encoding: utf-8 -*-
from django.db import models
from administration.models import Organisation
from administration.models import Domaine
from simple_history.models import HistoricalRecords

class Parcelle(models.Model):
    numIlot = models.IntegerField()
    nomParcelle = models.CharField(max_length=50)
    domaines = models.ManyToManyField(Domaine, through='ParcelleEtendue')
    appellation = models.CharField(max_length=50)       
    commune = models.CharField(max_length=50)
    refCadastre = models.CharField(max_length=50)
    anneesPlantation = models.CharField(max_length=50)
    datebio = models.CharField(max_length=50)
    history = HistoricalRecords()

    class Meta:
        db_table = "parcelles"

    def __str__(self):
        return self.nomParcelle

class Materiels(models.Model):
    nom = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        db_table = "materiels"

    def __str__(self):
        return self.nom

class ParcelleEtendue(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    proprietaire = models.CharField(max_length=50)
    surface = models.FloatField()

    class Meta:
        db_table = "parcelle-domaines"

    def __str__(self):
        return self.domaine + self.parcelle + self.proprietaire

class Cuve(models.Model):
    nom = models.CharField(max_length=20)
    contenanceMax = models.IntegerField()
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        db_table = "cuves"
    
    def __str__(self):
        return self.nom