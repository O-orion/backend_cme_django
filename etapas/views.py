from django.shortcuts import render
from rest_framework import viewsets
from .models import Etapa
from .serializers import EtapaSerializer

# Create your views here.
class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer