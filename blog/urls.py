from django.urls import path

from blog.views import index, ola #Nesta linha importamos as functions views.

urlpatterns = [
    path('index/', index, name="index"), # Define a rota /index
    path('ola/', ola, name="ola") #Define a rota /ola
]