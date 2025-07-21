from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from animais.models import Animal
from .models import PedidoAdocao
from .forms import PedidoAdocaoForm
from .utils import enviar_email_confirmacao_adocao  # importe no topo

@login_required
def solicitar_adocao(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = PedidoAdocaoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.animal = animal
            pedido.save()
            
            # Enviar e-mail de confirmação
            enviar_email_confirmacao_adocao(
                nome_usuario=request.user.first_name or request.user.username,
                email_usuario=request.user.email,
                nome_animal=animal.nome
            )

            return redirect('adocao:meus_pedidos')
    else:
        form = PedidoAdocaoForm()
    return render(request, 'adocao/solicitar.html', {'form': form, 'animal': animal})

@login_required
def meus_pedidos(request):
    status = request.GET.get('status')  # pega filtro da URL (opcional)
    pedidos = PedidoAdocao.objects.filter(usuario=request.user)

    if status in ['aguardando', 'aprovado', 'recusado']:
        pedidos = pedidos.filter(status=status)

    return render(request, 'adocao/meus_pedidos.html', {
        'pedidos': pedidos,
        'status_filtro': status
    })

@login_required
def cancelar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoAdocao, id=pedido_id, usuario=request.user)

    if pedido.status == 'aguardando':
        pedido.delete()
    return redirect('adocao:meus_pedidos')
