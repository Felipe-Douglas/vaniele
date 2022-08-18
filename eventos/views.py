from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html');

def login(request):
    return render(request, 'login.html');

def solicitacao(request):
    return render(request, 'solicitacao_evento.html')
