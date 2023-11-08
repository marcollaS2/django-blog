from django.db import models
import os
from uuid import uuid4


def safe_rename(instance, filename):  # função para renomear o arquivo de forma segura
    extension = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{extension}'
    return os.path.join('images', filename)


class Post(models.Model):
    body_text = models.TextField('Texto Principal')
    pub_date = models.DateTimeField('Data Publicação')


# Create your models here.
categoria = models.CharField(
    'Categoria',
    max_length=15,
    choices=[
        ('noticias', 'Notícias'),
        ('como_fazer', 'Como Fazer'),
        ('review', 'Review'),
    ],
    default=None,
    null=True
)

# oiiiiiii
