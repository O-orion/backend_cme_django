from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RastreabilidadeSerializer
from .models import Rastreabilidade

# Create your views here.
class RastreabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Rastreabilidade.objects.all()
    serializer_class = RastreabilidadeSerializer
