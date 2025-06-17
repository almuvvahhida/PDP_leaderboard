from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from student.models import Course, Group, Submission, SubmissionFiles
from student.serializers import CourseSerializer, GroupSerializer, SubmissionSerializer, SubmissionFilesSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.role.lower()

        if role == 'teacher':
            return Group.objects.filter(teacher=user)
        elif role == 'student':
            return Group.objects.filter(id=user.group.id)

        return Group.objects.all()

class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.role.lower()

        if role == 'teacher':
            return Submission.objects.filter()
        elif role == 'student':
            return Submission.objects.filter(student = user )

        return  Submission.objects.all()


class SubmissionFilesViewSet(ModelViewSet):
    queryset = SubmissionFiles.objects.all()
    serializer_class = SubmissionFilesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.role.lower()

        if role == 'teacher':
            return SubmissionFiles.objects.filter(submission__homework__group__teacher=user)
        elif role == 'student':
            return SubmissionFiles.objects.filter(submission__student=user)
        return SubmissionFiles.objects.all()