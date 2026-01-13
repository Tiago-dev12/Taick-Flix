from django.contrib import admin
from taickflix.models.cliente_model import Cliente
from django.contrib.auth.hashers import mask_hash

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'telefone', 'email', 'mask_senha')

    def mask_senha(self, cliente):
        return mask_hash(cliente.senha)
    
    readonly_fields = ('senha',)
