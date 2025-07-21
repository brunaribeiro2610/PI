from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(
        upload_to='blog/posts',
        null=True,
        blank=True,
        verbose_name='Imagem do post'
    )
    
    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo