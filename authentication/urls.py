from django.urls import path

from authentication.views import CustomTokenObtainPairView, CustomTokenRefreshView, SessionDestroyAPIView

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view()),
    path('session-drop/<int:session_pk>', SessionDestroyAPIView.as_view()),
    path('token/refresh/', CustomTokenRefreshView.as_view()),
]
