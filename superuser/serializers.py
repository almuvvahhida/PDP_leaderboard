from rest_framework.serializers import ModelSerializer, SerializerMethodField

from authentication.models import User


class UserSerializer(ModelSerializer):
    fullname = SerializerMethodField()

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'fullname', 'phone', 'avatar'  # 'group'
        read_only_fields = 'id', 'role'

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
