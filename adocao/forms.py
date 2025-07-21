from django import forms
from .models import PedidoAdocao

class PedidoAdocaoForm(forms.ModelForm):
    class Meta:
        model = PedidoAdocao
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Por que você quer adotar este animal?'}),
        }
