from django.contrib import admin
from .models import PedidoAdocao

class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'animal', 'status', 'criado_em')
    list_filter = ('status',)

admin.site.register(PedidoAdocao, PedidoAdocaoAdmin)
