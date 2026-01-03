from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from taickflix.forms.login_form import LoginForm
from taickflix.models.cliente_model import Cliente

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                cliente = Cliente.objects.get(email=email)
            except Cliente.DoesNotExist:
                return render(request, 'login.html', {'form' : form})

            if senha == cliente.senha:
                request.session['cliente_id'] = cliente.id
                return redirect('Home')
            else:
                return render(request, 'login.html', {'form' : form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})    
