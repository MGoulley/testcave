# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class Materiels(models.Model):
    nom = models.CharField(max_length=40)
    type = models.CharField(max_length=40)

    class Meta:
        db_table = "materiels"
