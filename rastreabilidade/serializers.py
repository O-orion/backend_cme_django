from rest_framework import serializers
from .models import Rastreabilidade

class RastreabilidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rastreabilidade
        db_table = 'rastreabilidade'
        fields = ['codigo_rastreio', 'codigo_usuario', 'codigo_artigo', 'codigo_etapa', 'data_inicio', 'status', 'falha', 'data_fim']
