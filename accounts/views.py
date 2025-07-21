from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/cadastro.html', {'form': form})

def entrar(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('core:home')  # ajuste o redirecionamento se necessário
        else:
            messages.error(request, 'Email ou senha inválidos.')
    return render(request, 'accounts/login.html')

def sair(request):
    logout(request)
    return redirect('core:index')

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')
