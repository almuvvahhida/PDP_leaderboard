from django.urls import path

from admin.views import SessionViewSet, TeacherViewSet
from student.views import GroupViewSet, CourseViewSet, SubmissionViewSet, SubmissionFilesViewSet

urlpatterns = [
    path('group/', GroupViewSet.as_view()),
    path('course/', CourseViewSet.as_view()),
    path('submission/', SubmissionViewSet.as_view()),
    path('submission-files/',SubmissionFilesViewSet.as_view()),
]
