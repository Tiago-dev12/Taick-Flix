from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from taickflix.models.cliente_model import Cliente
from phonenumber_field.formfields import PhoneNumberField

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=50, label='Nome')
    data_nascimento = forms.DateField(label='Dada de nascimento')
    telefone = PhoneNumberField(region='BR')
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')

        if senha:
            try:
                validate_password(senha)
            except ValidationError as e:
                self.add_error('senha', e)
        
        return cleaned_data
