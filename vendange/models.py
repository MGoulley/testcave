# -*- encoding: utf-8 -*-
from django.db import models
from entrants.models import Parcelle
from entrants.models import Materiels
from administration.models import Millesime
from administration.models import Organisation
from django.contrib.auth.models import User

class Benne(models.Model):
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    millesime = models.ForeignKey(Millesime, on_delete=models.CASCADE)
    operateur = models.ForeignKey(User, on_delete=models.CASCADE)
    benne = models.ForeignKey(Materiels, on_delete=models.CASCADE)
    parcelles = models.ManyToManyField(Parcelle, blank=True)
    idBenne = models.IntegerField()
    dateRecep = models.DateTimeField()
    densite = models.FloatField()
    temperature = models.FloatField()
    alcProb = models.FloatField()
    so2 = models.FloatField()
    commentaire = models.CharField(blank=True, max_length=40)
    meteo = models.CharField(max_length=10)
    pourcentSO2 = models.FloatField()

    class Meta:
        db_table = "benne"

class Marc(models.Model):
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    millesime = models.ForeignKey(Millesime, on_delete=models.CASCADE)
    idMarc = models.IntegerField()
    volumeMarc = models.FloatField(blank=True)
    pressoire = models.ForeignKey(Materiels, on_delete=models.CASCADE)
    bennes = models.ManyToManyField(Benne, through='BennesMarc')

    class Meta:
        db_table = "marc"


class BennesMarc(models.Model):
    marc = models.ForeignKey(Marc, on_delete=models.CASCADE)
    benne = models.ForeignKey(Benne, on_delete=models.CASCADE)
    volBenne = models.FloatField()

    class Meta:
        db_table = "bennes-marc"

    def __str__(self):
        return self.benne + self.volBenne