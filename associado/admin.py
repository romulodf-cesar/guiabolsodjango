from django.contrib import admin
from associado.models import Associado
from associado.models import Empresa

class ListandoAssociados(admin.ModelAdmin):
    list_display = ('nome', 'status', 'fk_empresa_id')
    search_fields = ('nome', 'status')

# Register your models here.
admin.site.register(Associado, ListandoAssociados)
admin.site.register(Empresa)
