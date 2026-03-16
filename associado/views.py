from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # um dicionário tem uma chave e um valor
    dados = {
        1:{
            "nome":"Rômulo",
            "Entidade":"Senai"
        },
        2:{
            "nome":"Milena",
            "Entidade":"Brasal"
        },
        3:{
            "nome":"Daniele",
            "entidade":"Brasal"
        },
        4:{
            "nome":"Erik",
            "entidade":"Café Export"
        }
    }
    # O Django buscará automaticamente dentro da pasta templates/
    return render(request,'associado/index.html' ,{"assoc":dados})
# Função para carregar o perfil do associado
def perfil(request):
    return render(request, 'associado/perfil.html')
def beneficios(request):
    # Por enquanto, apenas renderizamos o HTML de design
    return render(request, 'associado/beneficios.html')
def carteirinha(request):
    # Aqui passamos o contexto 'vibe pwa' para o template
    return render(request, 'associado/carteirinha.html')
