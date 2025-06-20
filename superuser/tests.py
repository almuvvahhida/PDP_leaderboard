import pytest
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient

from authentication.models import User, Session


class TestTeacher:
    @pytest.fixture  # clone database
    def api_client(self):
        user = User.objects.create(first_name="Ali",last_name="Aliyev",  phone="123456789", password=make_password("1"),
                                   role=User.RoleType.TEACHER.value)
        Session.objects.create(device_name="Linux 54", user=user, ip_address="127.9.8.1")
        return APIClient()

    @pytest.mark.django_db
    def test_login(self, api_client):
        response = api_client.post("http://localhost:8000/api/v1/login", {
            "phone": "993583231",
            "password": "1"
        }, format="json")
        assert isinstance(response.data, list) == True
        session_first_pk = response.data[0].get("id")
        delete_url = f'http://localhost:8000/api/v1/session-drop/{session_first_pk}'
        response = api_client.delete(delete_url)
        assert response.status_code == 204
        headers = {
            'User-Agent': 'CustomUserAgent/1.0',
            'X-Forwarded-For': '123.45.67.89',
        }
        response = api_client.post("http://localhost:8000/api/v1/login", {
            "phone": "993583231",
            "password": "1"
        }, headers=headers, format="json")
        assert response.status_code == 200
        assert isinstance(response.data, dict) == True
        assert "access" in response.data.keys() and "refresh" in response.data.keys()

    @pytest.mark.django_db
    def test_teacher_delete(self, api_client):
        pass

    @pytest.mark.django_db
    def test_teacher_edit(self, api_client):
        pass
