from django.shortcuts import render, redirect
from taickflix.decorators import cliente_login_required

@cliente_login_required
def home_view(request):
    return render(request, 'home.html')
