from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    telefone = PhoneNumberField(region='BR')
    email = models.EmailField(max_length=250, blank=False, null=False)
    senha = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome
