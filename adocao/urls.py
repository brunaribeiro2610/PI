from django.urls import path
from . import views

app_name = 'adocao'

urlpatterns = [
    path('solicitar/<int:animal_id>/', views.solicitar_adocao, name='solicitar'),
    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),
    path('cancelar/<int:pedido_id>/', views.cancelar_pedido, name='cancelar_pedido'),

]
