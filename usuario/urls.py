# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)  # A URL registrada será /usuario/

urlpatterns = [
    path('usuarios/', include(router.urls))  # Aqui deve ser /usuarios/ para corresponder ao que você quer
]
