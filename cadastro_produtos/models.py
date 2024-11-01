# /cadastro_produtos/models.py

from django.utils.timezone import now
# from datetime import timezone
from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_em_estoque = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=now)



    def __str__(self):
        return self.nome

    