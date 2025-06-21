import re

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from authentication.models import User


class UserSerializer(ModelSerializer):
    fullname = SerializerMethodField()

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'fullname', 'phone', 'avatar',  # 'group'
        read_only_fields = 'id', 'role',

    def validate_phone(self, value):
        pattern = r'^\+?\d{9,15}$'
        if not re.match(pattern, value):
            raise ValidationError('Invalid phone number format. Must start with "+" followed by 12 digits.')

        queryset = User.objects.filter(phone=value)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise ValidationError('User with this phone number already exists.')
        return value

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

# class GroupSerializer(ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ''
