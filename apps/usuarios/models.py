
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    codigo_user = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    codigo_papel = models.ForeignKey(Papel, on_delete=models.CASCADE, related_name='usuarios')
    date_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.nome