# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtigoViewSet

router = DefaultRouter()
router.register(r'artigo', ArtigoViewSet)  # A URL registrada será /usuario/

urlpatterns = [
    path('', include(router.urls))  # Aqui deve ser /usuarios/ para corresponder ao que você quer
]
