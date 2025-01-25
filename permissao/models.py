from django.db import models

# Create your models here.
class Permissao(models.Model):
    codigo_perm = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = 'permissao'
    
    
    def __str__(self):
        return self.nome