from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False, default='0000-00-00')
    telefone = models.FloatField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=False, null=False)
    senha = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome
