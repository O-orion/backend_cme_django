# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RastreabilidadeViewSet

router = DefaultRouter()
router.register(r'historico', RastreabilidadeViewSet)  # A URL registrada será /usuario/

urlpatterns = [
    path('', include(router.urls))  # Aqui deve ser /usuarios/ para corresponder ao que você quer
]
