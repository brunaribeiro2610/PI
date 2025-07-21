from django.db import models
from django.contrib.auth import get_user_model

class Animal(models.Model):
    ESPECIES = (
        ('Cão', 'Cão'),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
    )

    SEXO = (
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    )

    PORTE = (
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    )

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    raca = models.CharField(max_length=100, blank=True)
    idade = models.PositiveIntegerField(help_text="Idade aproximada (em anos)")
    sexo = models.CharField(max_length=6, choices=SEXO)
    porte = models.CharField(max_length=10, choices=PORTE)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='animais/')
    criado_por = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
