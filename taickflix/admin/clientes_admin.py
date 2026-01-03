from django.contrib import admin
from taickflix.models.cliente_model import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...
