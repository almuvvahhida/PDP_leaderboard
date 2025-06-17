from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, SET_NULL, ImageField
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField


# User override
# Session
class User(AbstractUser):
    class RoleType(TextChoices):
        STUDENT = 'Student', 'student'
        ADMIN = 'Admin', 'admin'
        TEACHER = 'Teacher', 'teacher'

    group = ForeignKey('student.Group', SET_NULL, related_name='users')
    role = CharField(max_length=15, choices=RoleType, default=RoleType.STUDENT)
    REQUIRED_FIELDS = []
    phone = CharField(max_length=15, unique=True)
    USERNAME_FIELD = 'phone'
    avatar = ImageField()