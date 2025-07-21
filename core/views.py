from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def contato(request):
    return render(request, 'core/contato.html')


# Create your views here.
