from django import forms
from .models import Benne
from parcelles.models import Parcelle
from django.db import models
import datetime
from django.utils.timezone import now

TIME_ZONE = 'Europe/London'

METEO_CHOICES = [
    ('EMPTY', 'Beau Temps'),
    ('INCOMPLETE', 'Pas beau'),
    ('COMPLETE', 'Neige'),
]

class BenneForm(forms.ModelForm):
    class Meta:
        model = Benne
        #exclude = ('parcelles',)
        fields = '__all__'


    idBenne = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    idMillesime = forms.IntegerField(initial='0000000', widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    dateRecep = forms.DateTimeField(initial=now, input_formats= ['%m/%d/%Y %H:%M'],
        widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M',
        attrs={
            'class': "form-control"
        }
    ))
    densite = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': "form-control"
        }
    ))
    temperature = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': "form-control"
        }
    ))
    alcProb = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': "form-control"
        }
    ))
    so2 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': "form-control"
        }
    ))
    autre1 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    autre2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    meteo = forms.ChoiceField(choices = METEO_CHOICES, label='Renseigner un champs', initial='', required=True, widget=forms.Select(
        attrs={
            'class': "form-control"
        }
    ))
    pourcentSO2 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': "form-control"
        }
    ))
    idOperateur = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    idMateriel = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
