from django.urls import path

from superuser.views import AdminTeacherListAPIView, AdminTeacherCreateAPIView, AdminTeacherUpdateAPIView, \
    AdminTeacherDestroyAPIView, AdminStudentListAPIView, AdminStudentCreateAPIView, AdminStudentUpdateAPIView, \
    AdminStudentDestroyAPIView

urlpatterns = [
    path('admin-teachers', AdminTeacherListAPIView.as_view()),
    path('admin-teacher/create', AdminTeacherCreateAPIView.as_view()),
    path('admin-teacher/<int:pk>/update', AdminTeacherUpdateAPIView.as_view()),
    path('admin-teacher/<int:pk>/delete', AdminTeacherDestroyAPIView.as_view()),
    path('admin-students', AdminStudentListAPIView.as_view()),
    path('admin-student/create', AdminStudentCreateAPIView.as_view()),
    path('admin-student/<int:pk>/update', AdminStudentUpdateAPIView.as_view()),
    path('admin-student/<int:pk>/delete', AdminStudentDestroyAPIView.as_view()),
]
