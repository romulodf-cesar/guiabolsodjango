from django.db import models
from django.core.exceptions import ValidationError

class Endereco(models.Model):
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    # Permite ligar a um Associado OU a uma Empresa
    associado = models.OneToOneField('Associado', on_delete=models.CASCADE, null=True, blank=True, related_name='endereco')
    empresa = models.OneToOneField('Empresa', on_delete=models.CASCADE, null=True, blank=True, related_name='endereco_empresa')

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"
    
    # definir o nome da tabela
    class Meta:
        db_table = 'endereco'
class Empresa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False,unique=True)  
   
    def clean(self):
        # Exemplo: remover pontos e traços antes de validar (caso o usuário digite com máscara)
        self.cnpj = ''.join(filter(str.isdigit, self.cnpj))
        
        # Verifica se já existe outra empresa com este CNPJ (excluindo a própria empresa em caso de edição)
        if Empresa.objects.filter(cnpj=self.cnpj).exclude(pk=self.pk).exists():
            raise ValidationError({'cnpj': "Já existe uma empresa cadastrada com este CNPJ."})
    def __str__(self):
        return self.nome+" - CNPJ: " + self.cnpj
    
    # definir o nome da tabela
    class Meta:
        db_table = 'empresa'


class Associado(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False,unique=True)
    ativo = models.BooleanField(default=True, null=False, blank=False)
    
   # Relação N:1 (Muitos associados para uma empresa)
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='associados'
    )

    def __str__(self):
        return self.nome+" - Ativo: " + str(self.ativo)
    
    # definir o nome da tabela
    class Meta:
        db_table = 'associado'

