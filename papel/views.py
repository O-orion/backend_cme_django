from django.shortcuts import render
from rest_framework import viewsets
from .models import Papeis
from .serializers import PapelSerializer

# Create your views here.
class PapelViewSet(viewsets.ModelViewSet):
    queryset = Papeis.objects.all()
    serializer_class = PapelSerializer