from rest_framework import serializers
from .models import Artigo
from datetime import date

class ArtigoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artigo
        fields = ['codigo_artigo', 'nome', 'tipo_material', 'data_validate', 'codigo_serial']

    
    def  validate_data_validate(self, value):
        if value < date.today():
            raise serializers.ValidationError("A data de validade não pode ser no passado.")
        return value