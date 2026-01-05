from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    sobrenome = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=False, null=False)
    telefone = models.FloatField(max_length=12, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome
