from rest_framework import serializers
from .models import Permissao

class PermissaoSerializer(serializers.ModelSerializer):
    model =  Permissao
    db_table = 'permissao'
    fields = ['codigo_perm', 'nome', 'descricao']