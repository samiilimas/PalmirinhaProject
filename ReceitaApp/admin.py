from django.contrib import admin
from django.utils.html import mark_safe

from ReceitaApp.models import Categoria
from ReceitaApp.models import Receita

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['id', 'nome']
    #colunas com link para editar
    list_display_links = ['nome']

class ReceitaAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['id', 'nome', 'ingredientes', 'modo_de_preparo', 'grau_de_dificuldade', 'categoria']
    #colunas com link para editar
    list_display_links = ['id', 'nome']
    #colunas para filtro
    list_filter = ['categoria']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)

