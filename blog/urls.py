from django.urls import path
from django.urls import path
from accounts import views

from blog.views import (
    index, ola, post_show, PostDetailView,
    get_all_posts, get_post,
    PostCreateView, create_post,
    PostListView,
    SobreTemplateView, )


urlpatterns = [
    path('index/', index, name="index"),
    path('ola/', ola, name='ola'),
    path('posts/all', ola, name='posts_list'),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name="post_detail"),
    path('api/post/add', create_post, name="create_post_data"),
    path('posts', PostListView.as_view(), name="posts_all")
    path('about-us',
        SobreTemplateView.as_view(),
        name="about_page"
),
]


urlpatterns = [
    path('accounts/signup', # caminho que vai carregar a view com o formulário
    views.AccountCreateView.as_view(),
    name="signup"
),
]
