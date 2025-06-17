from rest_framework import serializers

from student.models import Course, Group, Submission, SubmissionFiles


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class SubmissionFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionFiles
        fields = '__all__'