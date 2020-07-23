# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Domaine(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=50)

    class Meta:
        db_table = "domaines"

    def __str__(self):
        return self.nom

class Organisation(models.Model):
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)
    domaines = models.ManyToManyField(Domaine, blank=True)

    class Meta:
        db_table = "organisation"

    def __str__(self):
        return self.nom

class Millesime(models.Model):
    annee = models.IntegerField(primary_key=True)
    nomMillesime = models.CharField(max_length=20)
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    class Meta:
        db_table = "millesimes"

class Personnels(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orga = models.ForeignKey(Organisation, on_delete=models.CASCADE)