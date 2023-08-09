from django.shortcuts import render
from blog.models import Post 

# Incluir a classe HttpResponse.
from django.http import HttpResponse

# Define uma function view chamada index.
def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

# Define uma function view chamada ola.
# def ola(request):
    # return HttpResponse('Olá Django')
    return render(request, 'home.html')

def ola(request): # Modificar
# return HttpResponse('Olá django')
    posts = Post.objects.all() # recupera todos os posts do banco de dados
    context = {'posts_list': posts } # cria um dicionário com os dado
    return render(request, 'posts.html', context) # renderiza o template e passa o contexto
