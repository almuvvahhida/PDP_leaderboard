from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ForeignKey, ImageField, Model, CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, DateTimeField


class CustomerUser(UserManager):
    def _create_user_object(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("The given phone must be set")
        phone = ''.join(filter(str.isdigit, phone))[-15:]
        user = self.model(phone=phone, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)

    def _create_user(self, phone, password, **extra_fields):
        user = self._create_user_object(phone, password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class RoleType(TextChoices):
        STUDENT = 'Student', 'student'
        ADMIN = 'Admin', 'superuser'
        TEACHER = 'Teacher', 'teacher'

    username = None
    role = CharField(max_length=15, choices=RoleType, default=RoleType.STUDENT)
    phone = CharField(max_length=15, unique=True)
    # group = ForeignKey('student.Group', SET_NULL, blank=True, null=True, related_name='users')
    avatar = ImageField(upload_to='users/', null=True, blank=True)
    USERNAME_FIELD = 'phone'
    email = None
    REQUIRED_FIELDS = []
    objects = CustomerUser()


class Session(Model):
    user = ForeignKey('authentication.User', CASCADE, related_name='sessions')
    device_name = CharField(max_length=255)
    ip_address = CharField(max_length=20)
    last_login = DateTimeField(auto_now_add=True)
