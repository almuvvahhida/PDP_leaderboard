from rest_framework.serializers import ModelSerializer, SerializerMethodField

from admin.models import Session, User


class TeacherSerializer(ModelSerializer):
    fullname = SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'fullname', 'phone', 'avatar', 'group']
        read_only_fields = ['id', 'role']

    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()

    def create(self, validated_data):
        validated_data['role'] = User.RoleType.TEACHER
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['role'] = User.RoleType.TEACHER
        return super().update(instance, validated_data)


class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
