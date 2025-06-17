from django.db.models import Model, TextField, SmallIntegerField, CharField, DateField, IntegerField, ForeignKey

# HomeWork
"""Sababi"""
class HomeWork(Model):
    title = CharField(max_length=255)
    description = TextField()
    points = IntegerField()
    start_date = DateField()
    deadline = DateField()
    line_limit = SmallIntegerField(default=300)
    teacher_id = IntegerField(default=255)
    group_id = IntegerField(default=255)
    file_extension = CharField(max_length=255)
    ai_grading_prompt = TextField()
    created_at = DateField(auto_now_add=True)


# Grade

class Grades(Model):
    submissions_id = IntegerField(default=255)
    ai_task_completeness = SmallIntegerField(default=0)
    ai_code_quality = SmallIntegerField(default=0)
    ai_correctness = SmallIntegerField(default=0)
    ai_total = IntegerField(default=0)
    final_task_completeness = SmallIntegerField(default=0)
    final_code_quality = SmallIntegerField(default=0)
    final_correctness = SmallIntegerField(default=0)
    teacher_total = IntegerField(default=0)
    ai_feedback = TextField()
    task_completeness_feedback = TextField()
    code_quality_feedback = TextField()
    correctness_feedback = TextField()
    modified_by_teacher = TextField()
