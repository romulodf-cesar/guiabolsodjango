from django.urls import path
from associado.views import index,perfil,beneficios,carteirinha,empresa
urlpatterns = [
   path('',index,name='index'),
   path('perfil/', perfil, name='perfil'), # Rota amigável: /perfil/
   path('beneficios/',beneficios, name='beneficios'), # Nova rota!
   path('minha-carteirinha/',carteirinha, name='carteirinha'),
   path('empresa/',empresa,name='empresa')
]

