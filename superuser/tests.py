import pytest
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient

from authentication.models import User


class TestTeacher:
    @pytest.fixture
    def api_client(self):
        user = User.objects.create(
            first_name="zxcvbnm",
            last_name='qwertyuiop',
            phone="993583231",
            password=make_password("1"),
            role=User.RoleType.ADMIN,
            is_staff=True,
            is_superuser=True
        )
        client = APIClient()
        client.force_authenticate(user=user)
        return client

    @pytest.mark.django_db
    def test_create_teacher(self, api_client):
        response = api_client.post("/api/v1/admin-teacher/create", {
            'first_name': 'Alex',
            'last_name': 'Johnson',
            'phone': '234523629',
            'password': '1',
        }, format='multipart')

        print("Response: ", response.status_code, response.data)
        assert response.status_code == 201
        assert User.objects.filter(phone='234523629', role=User.RoleType.TEACHER).exists()

    @pytest.mark.django_db
    def test_teacher_list(self, api_client):
        User.objects.create(first_name='David', last_name='Johnson', phone='1234560987', role=User.RoleType.TEACHER)
        User.objects.create(first_name='Stefan', last_name='Salvatore', phone='1209876543', role=User.RoleType.STUDENT)
        response = api_client.get('/api/v1/admin-teachers')
        assert response.status_code == 200
        assert all(user['phone'] != '1209876543' for user in response.data)

    @pytest.mark.django_db
    def test_teacher_edit(self, api_client):
        user = User.objects.get(phone='993583231')
        response = api_client.put(
            f"http://localhost:8000/api/v1/admin-teachers/{user.pk}/update",
            {'first_name': 'updated', 'last_name': 'name', 'phone': '1234560987'}, format='json')

        assert response.status_code == 200
        user.refresh_from_db()
        assert user.first_name == 'updated'
        assert user.last_name == 'name'

    @pytest.mark.django_db
    def test_teacher_delete(self, api_client):
        user = User.objects.get(phone='993583231')
        response = api_client.delete(f"http://localhost:8000/api/v1/admin-teachers/{user.pk}/delete")
        assert response.status_code == 204
        assert not User.objects.filter(phone='993583231').exists()
