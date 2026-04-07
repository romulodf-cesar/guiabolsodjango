from django.contrib import admin
from .models import Empresa, Associado, Endereco

# 1. Configuração do Endereço para aparecer dentro de outras telas
class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1 # Define quantas caixinhas de endereço vazias aparecem por padrão
    max_num = 1 # Garante que só possa cadastrar um endereço (já que é OneToOne)

# 2. Configuração do Admin de Empresa
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj')
    list_display_links = ('nome', 'cnpj')
    
    # Adiciona o formulário de endereço dentro da página da Empresa
    inlines = [EnderecoInline]
    
    # Remove o campo 'associado' que existe no modelo Endereco para não confundir
    def get_inline_instances(self, request, obj=None):
        inline_instances = super().get_inline_instances(request, obj)
        for inline in inline_instances:
            if isinstance(inline, EnderecoInline):
                inline.exclude = ['associado'] # Esconde o campo associado no admin da Empresa
        return inline_instances

# 3. Configuração do Admin de Associado
@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'ativo')
    list_filter = ('ativo', 'empresa')
    search_fields = ('nome', 'cpf')

    # O dropdown de Empresa já aparece automaticamente por ser uma ForeignKey
    # Adicionamos o endereço aqui também
    inlines = [EnderecoInline]

    def get_inline_instances(self, request, obj=None):
        inline_instances = super().get_inline_instances(request, obj)
        for inline in inline_instances:
            if isinstance(inline, EnderecoInline):
                inline.exclude = ['empresa'] # Esconde o campo empresa no admin do Associado
        return inline_instances

