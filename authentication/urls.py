from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import CustomTokenObtainPairView, CustomTokenRefreshView, SessionDestroyAPIView

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view()),
    path('session-drop/<int:session_pk>', SessionDestroyAPIView.as_view()),
    path('token/refresh/', CustomTokenRefreshView.as_view()),
]
