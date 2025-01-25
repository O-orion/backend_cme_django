from django.db import models
from usuario.models import Usuario
from artigo.models import Artigo
from etapas.models import Etapa

# Create your models here.
class Rastreabilidade(models.Model):
    codigo_rastreio = models.AutoField(primary_key=True)
    codigo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="codigo_user", to_field="codigo_user", blank=False, null=False)
    codigo_artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, db_column="codigo_artigo", to_field="codigo_artigo")
    codigo_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, db_column="codigo_etapa", to_field="codigo_etapa")
    data_incio = models.DateField()
    status = models.CharField(max_length=255, null=False, blank=False)
    falha = models.BooleanField(default=False)
    data_fim = models.DateField()