from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from admin.models import Session, User
from admin.serializers import SessionSerializer, TeacherSerializer


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(role=User.RoleType.TEACHER)


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

