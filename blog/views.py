from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import AccountSignupForm  # importa o form de registro
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password  # para criptografar a senha
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, ListView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import PostModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

# Define uma function view chamada index.


@login_required
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_form.html'


# fields = ('body_text', ) # linha comentada pois o Form controla agora
success_url = ('posts_all')
form_class = PostModelForm
success_message = 'Postagem salva com sucesso.'


def form_valid(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super(PostCreateView, self).form_valid(request, *args, **kwargs)


User = get_user_model()  # obtém o model padrão para usuários do Django


class AccountCreateView(CreateView):
    model = User  # conecta o model a view
    template_name = 'registration/signup_form.html'  # template para o form HTML
    form_class = AccountSignupForm  # conecta o form a view
    # destino após a criação do novo usuário
    success_url = reverse_lazy('login')
    success_message = 'Usuário criado com sucesso!'


def form_valid(self, form):  # executa quando os dados estiverem válidos
    form.instance.password = make_password(form.instance.password)
    form.save()
    messages.success(self.request, self.success_message)
    return super(AccountCreateView, self).form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_form.html'
    # incluir os campos que deseja liberar a edição
    fields = ('first_name', 'email', 'imagem', )
    # rota para redirecionar após a edição
    success_url = reverse_lazy('posts_all')
    success_message = 'Perfil atualizado com sucesso!'


def get_queryset(self):  # método que altera o objeto recuperado pela view
    user_id = self.kwargs.get('pk')  # recupera o argumento vindo na URL / rota
    user = self.request.user  # obtém o objeto usuário da sessão
    if user is None or not user.is_authenticated or user_id != user.id:
        return User.objects.none()
        # apenas o usuário do perfil logado pode editar
        return User.objects.filter(id=user.id)


def form_valid(self, form):  # executa quando os dados estiverem válidos
    messages.success(self.request, self.success_message)

    return super(AccountUpdateView, self).form_valid(form)
