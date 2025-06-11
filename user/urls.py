from django.urls import path

from .views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name='user-register'),
    
    path('auth/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    
    path('auth/create-admin', UserViewSet.as_view({'post': 'create_admin'}), name='create-admin'),
    
    path('auth/me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
]