from django.db.models import CharField, ForeignKey, CASCADE, Model
from django.db.models.fields import DateTimeField, IntegerField, TextField


class Course(Model):
    name = CharField(max_length=255)


class Group(Model):
    name = CharField(max_length=255)
    teacher = ForeignKey('authentication.User', on_delete=CASCADE, related_name='teacher_groups')
    created_at = DateTimeField(auto_now=True)
    course = ForeignKey('student.Course', on_delete=CASCADE, related_name='groups')


class Submission(Model):
    homework = ForeignKey('teacher.HomeWork', on_delete=CASCADE, related_name='submissions')
    student = ForeignKey('authentication.User', on_delete=CASCADE, related_name='submissions')
    submitted_at = DateTimeField(auto_now=True)
    ai_grade = IntegerField()
    final_grade = IntegerField()
    final_grade_description = TextField()
    ai_feedback = TextField()
    created_at = DateTimeField(auto_now=True)


class SubmissionFiles(Model):
    submission = ForeignKey('student.Submission', on_delete=CASCADE, related_name='submissionfiles')
    file_name = CharField(max_length=255)
    content = CharField(max_length=255)
    line_count = IntegerField(null=True)
