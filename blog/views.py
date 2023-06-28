from django.shortcuts import render

# Incluir a classe HttpResponse.
from django.http import HttpResponse

# Define uma function view chamada index.
def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

# Define uma function view chamada ola.
def ola(request):
    return HttpResponse('Olá Django')
