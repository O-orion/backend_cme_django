from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from django.contrib import admin
from django.urls import path

urlpatterns = [
    # URLS JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('api/', include('usuario.urls')),
    path('api/', include('papel.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('artigo.urls')),
    path('api/', include('etapas.urls')),
]
