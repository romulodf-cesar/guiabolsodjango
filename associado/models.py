from django.db import models

# Create your models here.
class Associado(models.Model):
    LISTA_STATUS = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
        ('PENDENTE', 'Pendente'),
    ]
    nome = models.CharField(max_length=80,null=False,blank=False)
    status = models.CharField(max_length=15,null=False,blank=False,choices=LISTA_STATUS)
    # criar um atributo fk_empresa_id que seja uma chave estrangeira para a tabela empresa
    fk_empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True,verbose_name='Empresa')
    def __str__(self):
        return f"dados do objeto: {self.nome} - {self.fk_empresa_id} - {self.status}"
# faça uma chave estrangeira com empresa


class Empresa(models.Model):
    nome = models.CharField(max_length=80,null=False,blank=False)
    cnpj = models.CharField(max_length=16,null=False,blank=False)
    cidade = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return f"{self.nome}"    
