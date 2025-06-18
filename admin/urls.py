from django.urls import path, include
from rest_framework.routers import DefaultRouter

from admin.views import SessionViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'session', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
