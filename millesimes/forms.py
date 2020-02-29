from django import forms
from .models import Millesime

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
