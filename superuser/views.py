from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from authentication.models import User
from superuser.serializers import UserSerializer


@extend_schema(tags=['admin-teacher'])
class AdminTeacherListAPIView(ListAPIView):  # GET
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role=User.RoleType.TEACHER)


@extend_schema(tags=['admin-teacher'])
class AdminTeacherCreateAPIView(CreateAPIView):  # POST
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(role=User.RoleType.TEACHER)


@extend_schema(tags=['admin-teacher'])
class AdminTeacherUpdateAPIView(UpdateAPIView):  # PUT
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.filter(role=User.RoleType.TEACHER)
    lookup_field = 'pk'

    def get_queryset(self):
        return User.objects.filter(role=User.RoleType.TEACHER)


@extend_schema(tags=['admin-teacher'])
class AdminTeacherDestroyAPIView(DestroyAPIView):  # DELETE
    serializer_class = UserSerializer
    queryset = User.objects.filter(role=User.RoleType.TEACHER)
    lookup_field = 'pk'


@extend_schema(tags=['admin-student'])
class AdminStudentListAPIView(ListAPIView):  # GET
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role=User.RoleType.STUDENT)


@extend_schema(tags=['admin-student'])
class AdminStudentCreateAPIView(CreateAPIView):  # POST
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(role=User.RoleType.STUDENT)


@extend_schema(tags=['admin-student'])
class AdminStudentUpdateAPIView(UpdateAPIView):  # PUT
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.filter(role=User.RoleType.STUDENT)
    lookup_field = 'pk'

    def get_queryset(self):
        return User.objects.filter(role=User.RoleType.STUDENT)


@extend_schema(tags=['admin-student'])
class AdminStudentDestroyAPIView(DestroyAPIView):  # DELETE
    serializer_class = UserSerializer
    queryset = User.objects.filter(role=User.RoleType.STUDENT)
    lookup_field = 'pk'
