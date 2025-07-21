from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    ordering = ['-data_publicacao']

admin.site.register(Post, PostAdmin)
