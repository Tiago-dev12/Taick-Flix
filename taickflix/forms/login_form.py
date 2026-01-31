from django import forms
from taickflix.models.cliente_model import Cliente

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'input'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'input'}))
