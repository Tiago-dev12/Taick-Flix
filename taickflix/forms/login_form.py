from django import forms
from taickflix.models.cliente_model import Cliente
import hashlib


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

    '''
    def clean_email(self):
        email = self.cleaned_data.get('email').strip()
        if not Cliente.objects.filter(email=email).exists():
            raise forms.ValidationError('Emial inválido.')
        return email
    
    def clean_senha(self):
        senha = self.cleaned_data.get('senha').strip()
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        if not Cliente.objects.filter(senha=hash_senha):
            raise forms.ValidationError('Senha inválida.')
        return senha
    '''
