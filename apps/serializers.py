import re

from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from apps.models import User


class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'fullname', 'phone', 'role', 'password',

    def validate(self, attrs):
        passwd = make_password(attrs.get('password'))
        attrs['password'] = passwd
        return super().validate(attrs)

    def validate_phone(self, value):
        return re.sub(r'\D', '', value)


