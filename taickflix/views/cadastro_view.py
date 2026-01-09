from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from taickflix.models import Cliente
from taickflix.forms  import CadastroForm

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']
            especiais = '~!@#$%^&*()+{}":;\'[]'

            if any(c in especiais for c in nome):
                form.add_error('nome', 'Use apenas letras e/ou números')

            if Cliente.objects.filter(email=email):
                form.add_error('email', 'Este email já etsá cadastrado')
            
            if senha != confirmar_senha:
                form.add_error('confirmar_senha', 'As senhas precisam ser iguais')

            if not form.errors:
                usuario = Cliente(
                    nome = nome,
                    data_nascimento = data_nascimento,
                    telefone = telefone,
                    email = email,
                    senha = senha
                )
                usuario.save()

                signer = TimestampSigner()
                token = signer.sign(email)
                link = f'http://127.0.0.1:8000/confirmar-email/?token={token}'

                send_mail(
                    'Confirme seu email para se cadastrar na TaickFlix',
                    f"Clique neste link para confirmar: \n{link}",
                    'no-reply@taickflix.com',
                    [email],
                )

    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})
