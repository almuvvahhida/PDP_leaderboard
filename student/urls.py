from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from student.views import GroupViewSet, CourseViewSet, SubmissionViewSet, SubmissionFilesViewSet

urlpatterns = [
    path('group/', GroupViewSet.as_view()),
    path('course/', CourseViewSet.as_view()),
    path('submission/', SubmissionViewSet.as_view()),
    path('submission-files/',SubmissionFilesViewSet.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
