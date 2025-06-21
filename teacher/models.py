from django.db.models import Model, TextField, SmallIntegerField, CharField, DateField

class HomeWork(Model):
    title = CharField(max_length=255)
    description = TextField()
    points = SmallIntegerField(default=0)
    start_date = DateField()
    deadline = DateField()
    line_limit = SmallIntegerField(default=300)

# Grade
