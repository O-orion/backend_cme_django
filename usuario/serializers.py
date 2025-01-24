from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['codigo','nome', 'email', 'password', 'codigo_papel', 'date_created']
        extra_kwargs  = {
            'senha_hash': {'write_only': True}
        }
