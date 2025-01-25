from rest_framework import serializers
from .models import PapelPermissao

class PapelPermissaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PapelPermissao
        db_table = 'papel_permissao'
        fields = ['codigo', 'codigo_papel', 'codigo_perm']