from django.urls import path

from admin.views import SessionViewSet, TeacherViewSet

urlpatterns = [
    path('teacher', TeacherViewSet.as_view()),
    path('session', SessionViewSet.as_view()),
]
