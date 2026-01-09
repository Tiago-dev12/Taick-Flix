from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.http import HttpResponse
from django.shortcuts import render, redirect
from taickflix.models import Cliente

def confirm_email_view(request):
    token = request.GET.get('token')
    signer = TimestampSigner()

    try:
        email = signer.unsign(token, max_age=60*30)
        usuario = Cliente.objects.get(email=email)
        usuario.ativo = True
        usuario.save()
    except SignatureExpired:
        return HttpResponse("link expirado.")
    except BadSignature:
        return HttpResponse("link inválido.")
    
    return render(request, 'email_confirmado.html')
        
