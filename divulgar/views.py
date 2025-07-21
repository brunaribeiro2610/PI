from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnimalDivulgadoForm
from .models import AnimalDivulgado

@login_required
def divulgar_animal(request):
    if request.method == 'POST':
        form = AnimalDivulgadoForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.criado_por = request.user
            animal.save()
            return redirect('divulgar:meus_animais')
    else:
        form = AnimalDivulgadoForm()
    return render(request, 'divulgar/divulgar.html', {'form': form})

@login_required
def meus_animais(request):
    animais = AnimalDivulgado.objects.filter(criado_por=request.user)
    return render(request, 'divulgar/meus_animais.html', {'animais': animais})
