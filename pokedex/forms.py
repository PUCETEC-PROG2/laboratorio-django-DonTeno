from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name' : 'Nombre',
            'type' : 'Tipo',
            'height' : 'Altura',
            'weight' : 'Peso',
            'trainer' : 'Entrenador',
            'picture' : 'Foto'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }