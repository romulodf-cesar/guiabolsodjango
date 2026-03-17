from django.db import models

# Create your models here.
class Associado(models.Model):
    nome = models.CharField(max_length=80,null=False,blank=False)
    entidade = models.CharField(max_length=80,null=False,blank=False)
    status = models.CharField(max_length=60,null=False,blank=False)

    def __str__(self):
        return f"dados do objeto: {self.nome} - {self.entidade} - {self.status}"

