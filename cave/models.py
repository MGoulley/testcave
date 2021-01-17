# -*- encoding: utf-8 -*-
from django.db import models
from simple_history.models import HistoricalRecords
from vendange.models import Marc
from administration.models import Organisation
from administration.models import Millesime

class Lot(models.Model):
    nom = models.CharField(max_length=20)
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    volume = models.FloatField()
    marc = models.ManyToManyField(Marc, through='MarcsLots', blank=True)
    millesime = models.ForeignKey(Millesime, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField()
    history = HistoricalRecords()

    class Meta:
        db_table = "lots"

    def __str__(self):
        return self.nom

class MarcsLots(models.Model):
    marc = models.ForeignKey(Marc, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    volume = models.FloatField()

    class Meta:
        db_table = "marcs-lots"

    def __str__(self):
        return self.marc + self.lot + self.volume

class Operation(models.Model):
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    millesime = models.ForeignKey(Millesime, on_delete=models.CASCADE)
    dateAction = models.DateTimeField()
    history = HistoricalRecords()

    class Meta:
        db_table = "operations"

    def __str__(self):
        return self.orga + self.millesime + self.dateAction

class Assemblage(Operation):
    lots = models.ManyToManyField(Lot, through='AssemblageLots', blank=True)
    history = HistoricalRecords()

    class Meta:
        db_table = "assemblages"

    def __str__(self):
        return self.orga + self.millesime + self.dateAction

class AssemblageLots(models.Model):
    assemblage = models.ForeignKey(Assemblage, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    volume = models.FloatField()

    class Meta:
        db_table = "assemblage-lots"

    def __str__(self):
        return self.lot + self.volume