# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtapaViewSet

router = DefaultRouter()
router.register(r'etapas', EtapaViewSet)  

urlpatterns = [
    path('', include(router.urls))
]
