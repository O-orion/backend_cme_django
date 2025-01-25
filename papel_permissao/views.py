from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PapelPermissaoSerializer
from .models import PapelPermissao


# Create your views here.
class PapelPermissaoViewSet(viewsets.ModelViewSet):
    queryset = PapelPermissao.objects.all()
    serializer_class = PapelPermissaoSerializer