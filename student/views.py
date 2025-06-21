from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from student.models import Course, Group, Submission, SubmissionFiles
from student.serializers import CourseSerializer, GroupSerializer, SubmissionSerializer, SubmissionFilesSerializer


class CourseViewSet(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(ListAPIView):
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

class SubmissionViewSet(CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionFilesViewSet(ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionFilesSerializer

    def get_queryset(self):
        user = self.request.user
        role = user.role.lower()

        if role == 'teacher':
            return SubmissionFiles.objects.filter(submission__homework__group__teacher=user)
        elif role == 'student':
            return SubmissionFiles.objects.filter(submission__student=user)
        return SubmissionFiles.objects.all()