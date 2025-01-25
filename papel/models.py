from django.db import models

# Create your models here.
class Papeis(models.Model):
    codigo_papel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'papeis'
    def __str__(self):
        return self.nome


