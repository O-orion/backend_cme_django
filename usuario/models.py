from django.db import models
from papel.models import Papeis
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Usuario(models.Model):
    codigo_user = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    passwordhash = models.CharField(max_length=255)
    codigo_papel = models.ForeignKey(Papeis, on_delete=models.CASCADE, db_column='codigo_papel', to_field='codigo_papel')
    #data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nome

    def set_password(self, raw_password):
        self.passwordhash = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.passwordhash)
