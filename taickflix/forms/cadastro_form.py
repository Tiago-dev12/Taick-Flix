from django import forms
from taickflix.models.cliente_model import Cliente

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=50, label='Nome')
    data_nascimento = forms.DateField(label='Dada de nascimento')
    telefone = forms.IntegerField(label='N° do telefone')
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
