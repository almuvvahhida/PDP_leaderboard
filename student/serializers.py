from rest_framework import serializers

from student.models import Course, Group, Submission, SubmissionFiles


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'name',


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'id', 'name', 'teacher_id', 'created_at', 'course_id',


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = 'id', 'homework', "student", 'submitted_at', 'ai_grade', 'final_grade', 'final_grade_description', 'ai_feedback', 'created_at',


class SubmissionFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionFiles
        fields = 'id', 'submission', 'file_name', 'content', 'line_count',
