from django import forms
from .models import *

TYPE_CHOICES = [
    ('BENNE', 'Benne'),
    ('PRESSOIR', 'Pressoir'),
    ('AUTRE', 'Autre'),
]

APPELATIONS = [
    ('Petit Chablis', 'Petit Chablis'),
    ('Chablis', 'Chablis'),
    ('Premier Cru Fourchaume', 'Premier Cru Fourchaume'),
    ('Premier Cru Mont de Milieu', 'Premier Cru Mont de Milieu'),
    ('Premier Cru Montmains', 'Premier Cru Montmains'),
]

class ParcelleForm(forms.ModelForm):
    class Meta:
        model = Parcelle
        fields = '__all__'

    numIlot = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    nomParcelle = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    appellation = forms.ChoiceField(choices = APPELATIONS, label='Renseigner un champs', initial='', required=True, widget=forms.Select(
        attrs={
            'class': "form-control"
        }
    ))
    proprietaire = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    surface = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    commune = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    refCadastre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    anneesPlantation = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    datebio = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))

class MaterielsForm(forms.ModelForm):
    class Meta:
        model = Materiels
        fields = '__all__'

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    type = forms.ChoiceField(choices = TYPE_CHOICES, label='Renseigner un champs', initial='', required=True, widget=forms.Select(
        attrs={
            'class': "form-control"
        }
    ))