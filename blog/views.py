from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    """
    View para listar todos os posts do blog ordenados por data de publicação.
    """
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'blog/lista.html', {'posts': posts})

def detalhe_post(request, slug):
    """
    View para exibir um post específico e sugerir outros posts relacionados.
    """
    post = get_object_or_404(Post, slug=slug)
    outros_posts = (Post.objects
                   .exclude(pk=post.pk)
                   .order_by('-data_publicacao')[:5])
    
    context = {
        'post': post,
        'outros_posts': outros_posts
    }
    
    return render(request, 'blog/detalhe.html', context)