from django.http import HttpResponse
from django.shortcuts import render
from associado.models import Associado,Empresa
from django.db.models import Q

def index(request):
    # um dicionário tem uma chave e um valor
    """
      dados = {
        1:{
            "nome":"Rômulo",
            "entidade":"Senai",
            "status":"ativo"
        },
        2:{
            "nome":"Milena",
            "entidade":"Brasal",
            "status":"inativo"
        },
        3:{
            "nome":"Daniele",
            "entidade":"Brasal",
            "status": "pendente"
        },
        4:{
            "nome":"Erik",
            "entidade":"Café Export",
            "status":"ativo"
        },
        5:{
            "nome":"Artur",
            "entidade":"Brasal",
            "status":"inativo"
        },
        6:{
            "nome":"Mônica",
            "entidade":"Brasal",
            "status":"ativo"
        }
    }    
    
    """
    query = request.GET.get('q')
    if query:
        associados = Associado.objects.filter(
            Q(nome__icontains=query) | Q(fk_empresa_id__orgao__icontains=query)
        )
    else:
        associados = Associado.objects.all()
  
    # Estatisticas
    stats = {
        #"ativos": Associado.objects.filter(status="ATIVO").count(),
        #"pendentes": Associado.objects.filter(status="PENDENTE").count(),
        #"inativos": Associado.objects.filter(status="INATIVO").count()
    }
    # O Django buscará automaticamente dentro da pasta templates/
    return render(request,'associado/index.html' ,{"assoc":associados, "busca":query, "stats":stats})

# Função para carregar o perfil do associado
def perfil(request):
    return render(request, 'associado/perfil.html')
def beneficios(request):
    # Por enquanto, apenas renderizamos o HTML de design
    return render(request, 'associado/beneficios.html')
def carteirinha(request):
    # Aqui passamos o contexto 'vibe pwa' para o template
    return render(request, 'associado/carteirinha.html')

def empresa(request):
    # empresas = Empresa.objects.all()
    return render(request,'associado/empresa.html')
