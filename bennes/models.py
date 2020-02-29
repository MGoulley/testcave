# -*- encoding: utf-8 -*-
from django.db import models
from parcelles.models import Parcelle
# Create your models here.
class Benne(models.Model):
    idBenne = models.IntegerField()
    idMillesime = models.IntegerField()
    dateRecep = models.DateTimeField()
    densite = models.FloatField()
    temperature = models.FloatField()
    alcProb = models.FloatField()
    so2 = models.FloatField()
    autre1 = models.CharField(blank=True, max_length=40)
    autre2 = models.CharField(blank=True, max_length=40)
    meteo = models.CharField(max_length=10)
    pourcentSO2 = models.FloatField()
    idOperateur = models.IntegerField()
    idMateriel = models.IntegerField()
    parcelles = models.ManyToManyField(Parcelle, blank=True)

    class Meta:
        db_table = "benne"

    def __str__(self):
        #return self.parcelles.all().values_list('nomParcelle', flat=True)
        return '-'.join([str(i) for i in self.parcelles.all().values_list('nomParcelle', flat=True)])
        #return " ".join(list(self.parcelles.all()))
