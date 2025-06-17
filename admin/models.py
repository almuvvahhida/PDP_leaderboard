from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ForeignKey, SET_NULL, ImageField, Model, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DateTimeField, GenericIPAddressField


class CustomerUser(UserManager):
    def _create_user_object(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        user = self._create_user_object(email, password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class RoleType(TextChoices):
        STUDENT = 'Student', 'student'
        ADMIN = 'Admin', 'admin'
        TEACHER = 'Teacher', 'teacher'

    role = CharField(max_length=15, choices=RoleType.choices, default=RoleType.STUDENT)
    phone = CharField(max_length=15, unique=True)
    group = ForeignKey('student.Group',SET_NULL , null = True, related_name='users')
    avatar = ImageField()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = CustomerUser()


class Session(Model):
    user = ForeignKey('admin.User', CASCADE, related_name='sessions')
    token = CharField(max_length=255, unique=True)
    device_name = CharField(max_length=100)
    ip_address = GenericIPAddressField()
    last_login = DateTimeField(auto_now=True)
    expires_at = DateTimeField()
