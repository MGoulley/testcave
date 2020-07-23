from django import forms
from .models import Domaine
from .models import Millesime
from .models import Organisation
from django.db import models
import datetime
from django.utils.timezone import now

class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = '__all__'


    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))

    adresse = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))


class MillesimeForm(forms.ModelForm):
    class Meta:
        model = Millesime
        fields = '__all__'

    annee = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    nomMillesime = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))