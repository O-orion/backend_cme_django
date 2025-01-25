from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['codigo_user','nome', 'email', 'passwordhash', 'codigo_papel']
        extra_kwargs  = {
            'senha_hash': {'write_only': True}
        }

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        password = validated_data.pop('passwordhash', None)

        if password:
            usuario.set_password(password)
        
        usuario.save()
        return usuario
