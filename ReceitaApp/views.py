from django.shortcuts import render
from ReceitaApp.models import Receita, Categoria

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias' : categorias
    }

    return render(request, 'index.html', context)

def listar_receitas(request):
    
    receitas = Receita.objects.all()

    #dicionario que vai levar os dados para a template
    #chave : valor (ex.: 'cep' : 08010101)
    
    context = {
        'receitas' : receitas
    }

    #qual template essa view vai retornar
    return render(request, 'receitas.html', context)

def detalhes_receita(request, id):
    #buscando a receita correspondente ao id informado
    receita = Receita.objects.get(id = id)
    
    context = {
        'receita' : receita
    }
    return render(request, 'receita.html', context)