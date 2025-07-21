from django.shortcuts import render, get_object_or_404
from .models import Animal

def lista_animais(request):
    animais = Animal.objects.all()

    especie = request.GET.get('especie')
    sexo = request.GET.get('sexo')
    porte = request.GET.get('porte')

    if especie:
        animais = animais.filter(especie=especie)
    if sexo:
        animais = animais.filter(sexo=sexo)
    if porte:
        animais = animais.filter(porte=porte)

    context = {'animais': animais}
    return render(request, 'animais/lista.html', context)

def detalhe_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animais/detalhe.html', {'animal': animal})
