import pytest
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient

from authentication.models import User


class TestTeacher:
    @pytest.fixture
    def api_client(self):
        user = User.objects.create(first_name="Ali", last_name="Aliyev", phone="123456789", password=make_password("1"),
                                   role=User.RoleType.TEACHER.value)
        return APIClient()

    @pytest.mark.django_db
    def test_create_teacher(self, api_client):
        response = api_client.post("http://localhost:8000/api/v1/admin-teacher/create", {
            "phone": "123456789",
            "password": "1"
        }, format="multipart")
        assert response.status_code == 201


    @pytest.mark.django_db
    def test_teacher_delete(self, api_client):
        pass

    @pytest.mark.django_db
    def test_teacher_edit(self, api_client):
        pass
