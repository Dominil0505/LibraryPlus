from django.urls import path

from djoser.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name='user-register'),
    
    path('auth/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    
    path('auth/me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
]