# usuario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PapelViewSet

router = DefaultRouter()
router.register(r'papel', PapelViewSet)  

urlpatterns = [
    path('papeis/', include(router.urls))
]
