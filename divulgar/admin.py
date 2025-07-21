from django.contrib import admin
from .models import AnimalDivulgado

class AnimalDivulgadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'criado_por', 'publicado')
    list_filter = ('publicado', 'especie')

admin.site.register(AnimalDivulgado, AnimalDivulgadoAdmin)
