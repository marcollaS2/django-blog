from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import PostModelForm


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

# Define uma function view chamada index.


def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

# Define uma function view chamada ola.
# def ola(request):
    # return HttpResponse('Olá Django')
    return render(request, 'home.html')


def ola(request):  # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all()  # recupera todos os posts do banco de dados
    context = {'posts_list': posts}  # cria um dicionário com os dado
    # renderiza o template e passa o contexto
    return render(request, 'posts.html', context)


class PostDetailView(DetailView):

    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


class SobreTemplateView(TemplateView):
    template_name = 'post/sobre.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_form.html'


# fields = ('body_text', ) # linha comentada pois o Form controla agora
success_url = reverse_lazy('posts_list')
form_class = PostModelForm
