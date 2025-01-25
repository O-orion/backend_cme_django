from django.db import models

# Create your models here.
class Artigo(models.Model):
    codigo_artigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null= False, blank=False)
    tipo_material = models.CharField(max_length=250, null=False, blank=False)
    data_validate = models.DateField(null=False)
    codigo_serial = models.CharField(max_length=288, null=False, blank=False)
    class Meta:
        db_table = 'artigo'

    def __str__(self):
        return self.nome