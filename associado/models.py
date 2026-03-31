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
    orgao = models.CharField(max_length=80,null=False,blank=False)
    cnpj = models.CharField(max_length=16,null=False,blank=False)
    ativo = models.BooleanField(default=True)
    sigla_orgao = models.CharField(max_length=10,null=True,blank=True)
    nome_contato = models.CharField(max_length=80,null=True,blank=True)
    endereco = models.CharField(max_length=60,null=True,blank=True)
    bairro = models.CharField(max_length=60,null=True,blank=True)   
    cidade = models.CharField(max_length=60,null=True,blank=True)
    """
       PascalCasing: Empresa, Associado
       camelCase: empresa, associado
       SNAKE_CASE: UF_CHOICES, LISTA_STATUS
       UPPERCASE: SECRET_KEY, DEBUG
    
    
    """
    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]
    uf = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        default='DF',
        verbose_name="UF"
    )
    cep = models.CharField(max_length=10,null=True,blank=True)
    telefone = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=80,null=True,blank=True)  
    def __str__(self):
        return f"{self.orgao}"  
    
