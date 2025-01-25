from django.db import models

# Create your models here.
class Etapa(models.Model):
    codigo_etapa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao =  models.CharField(max_length=255, null=False, blank=False)