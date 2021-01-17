from django import forms
from .models import *
from django.utils.timezone import now

class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = '__all__'

    nom = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))

    volume = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))

    millesime = forms.IntegerField(initial='0000000', disabled=True, widget=forms.TextInput(
        attrs={
            'class': "form-control"
        }
    ))

    dateCreation = forms.DateTimeField(initial=now, input_formats= ['%m/%d/%Y %H:%M'],
        widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M',
        attrs={
            'class': "form-control"
        }
    ))