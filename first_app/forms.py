from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model =models.Musician
        fields = ['first_name']
        #exclude=['last_name']
        #fields="__all__"



