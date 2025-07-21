from django import forms
from .models import AnimalDivulgado

class AnimalDivulgadoForm(forms.ModelForm):
    class Meta:
        model = AnimalDivulgado
        exclude = ['criado_por', 'publicado', 'criado_em']
