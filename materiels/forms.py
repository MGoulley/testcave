from django import forms
from .models import Materiels

TYPE_CHOICES = [
    ('BENNE', 'Benne'),
    ('PRESSOIR', 'Pressoir'),
    ('AUTRE', 'Autre'),
]

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
