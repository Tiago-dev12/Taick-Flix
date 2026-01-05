from django import forms
from taickflix.models.cliente_model import Cliente

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
