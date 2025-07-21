from django.urls import path
from . import views

app_name = 'divulgar'

urlpatterns = [
    path('novo/', views.divulgar_animal, name='novo'),
    path('meus/', views.meus_animais, name='meus_animais'),
]
