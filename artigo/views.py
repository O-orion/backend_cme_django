from django.shortcuts import render
from rest_framework import viewsets
from .models import Artigo
from .serializers import ArtigoSerializer

# Create your views here.
class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer