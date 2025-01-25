from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PermissaoSerializer
from .models import Permissao

# Create your views here.
class PermissaoViewSet(viewsets.ModelViewSet):
    queryset = Permissao.objects.all()
    serializer_class = PermissaoSerializer