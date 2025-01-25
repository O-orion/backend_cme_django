from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from usuario.models import Usuario
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny]) 
def login_usuario(request):

    # Autenticando usuário pelo email é senha
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or  not password:
        return Response({'ERROR: Por-favor, informa seu e-mail e sua senha!'})
    
    usuario = Usuario.objects.filter(email=email).first()

    if usuario and usuario.check_password(password):
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'usuario': {
                'codigo_user': usuario.codigo_user,
                'nome': usuario.nome,
                'email': usuario.email,
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'detail': 'Credenciais inválidas'
        }, status=status.HTTP_401_UNAUTHORIZED)