from django.db import models
from django.contrib.auth import get_user_model
from animais.models import Animal

User = get_user_model()

class PedidoAdocao(models.Model):
    STATUS_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')
    mensagem = models.TextField(blank=True, null=True) 
    criado_em = models.DateTimeField(auto_now_add=True)  # ⬅️ Adicionado aqui

    def __str__(self):
        return f'{self.usuario} - {self.animal}'
