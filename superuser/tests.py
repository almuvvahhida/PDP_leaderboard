import pytest
from rest_framework.test import APIClient

from authentication.models import User


class TestTeacher:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.mark.django_db
    def test_create_teacher(self, api_client):
        response = api_client.post("http://localhost:8000/api/v1/admin-teacher/create", {
            'first_name': 'Alex',
            'last_name': 'Johnson',
            'phone': '123456780',
            'password': '1',
        }, format='multipart')

        print("Response: ", response.status_code, response.data)
        assert response.status_code == 201
        assert User.objects.filter(phone='123456780', role=User.RoleType.TEACHER).exists()

    @pytest.mark.django_db
    def test_teacher_list(self, api_client):
        User.objects.create(first_name='David', last_name='Johnson', phone='1234560987', role=User.RoleType.TEACHER)
        User.objects.create(first_name='Stefan', last_name='Salvatore', phone='1209876543', role=User.RoleType.STUDENT)
        response = api_client.get('/api/v1/admin-teachers')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_teacher_edit(self, api_client):
        teacher = User.objects.create(first_name='David', last_name='Johnson', phone='1234560987', role=User.RoleType.TEACHER)

    @pytest.mark.django_db
    def test_teacher_delete(self, api_client):
        pass


