from django.db import models
from permissao.models import Permissao
from papel.models import Papeis

# Create your models here.
class PapelPermissao(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_papel = models.ForeignKey(Papeis, on_delete=models.CASCADE, db_column='codigo_papel', to_field="codigo_papel", null=False, blank=False)
    codigo_perm = models.ForeignKey(Permissao, on_delete=models.CASCADE, db_column='codigo_perm', to_field="codigo_perm", null=False, blank=False)