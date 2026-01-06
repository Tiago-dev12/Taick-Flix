from django.shortcuts import render, redirect

def cadastro_view(request):
    return render(request, 'cadastro.html')
