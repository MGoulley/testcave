from django import forms
from .models import Parcelle


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
    appellation = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    domaine = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
    surface = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))
