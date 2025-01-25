from rest_framework import serializers
from .models import Papeis

class PapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papeis
        db_table = 'papeis' 
        fields = ['codigo_papel', 'nome', 'descricao']
