
from rest_framework import serializers
from .models import Etapa

class EtapaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etapa
        db_table="etapas"
        fields=['codigo_etapa', 'nome', 'descricao']

