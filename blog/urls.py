from django.urls import path
from . import views

app_name = 'blog'  # Importante para usar 'blog:detalhe' e 'blog:lista'

urlpatterns = [
    path('', views.lista_posts, name='lista'),
    path('<slug:slug>/', views.detalhe_post, name='detalhe'),
]