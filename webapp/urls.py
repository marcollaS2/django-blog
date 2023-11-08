from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # rotas personalizadas como accounts/signup
    path('', include('accounts.urls')),
    # rotas fornecidas pelo Django
    path('accounts/', include('django.contrib.auth.urls')), path('account/<int:pk>/edit',
                                                                 views.AccountUpdateView.as_view(),
                                                                 name="account_edit"
                                                                 ),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
