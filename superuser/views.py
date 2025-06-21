from django.db import transaction
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser

from authentication.models import User
from superuser.serializers import UserSerializer


@extend_schema(tags=['admin-teacher'])
class AdminTeacherListAPIView(ListAPIView):  # GET
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(role=User.RoleType.TEACHER)
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'phone']


@extend_schema(tags=['admin-teacher'], request=UserSerializer, responses={201: UserSerializer},
               examples=[OpenApiExample('Example Teacher Creation', value={
                   'fullname': 'John Doe',
                   'phone': '1276358167',
                   'avatar': 'example.jpg'
               }, request_only=True)])
class AdminTeacherCreateAPIView(CreateAPIView):  # POST
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(role=User.RoleType.TEACHER)


@extend_schema(tags=['admin-teacher'])
class AdminTeacherUpdateAPIView(UpdateAPIView):  # PUT
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.filter(role=User.RoleType.TEACHER)
    lookup_field = 'pk'


@extend_schema(tags=['admin-teacher'])
class AdminTeacherDestroyAPIView(DestroyAPIView):  # DELETE
    serializer_class = UserSerializer
    queryset = User.objects.filter(role=User.RoleType.TEACHER)
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        if not instance:
            raise NotFound('Teacher not found.')
        instance.delete()


@extend_schema(tags=['admin-student'])
class AdminStudentListAPIView(ListAPIView):  # GET
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'phone']

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


@extend_schema(tags=['admin-student'])
class AdminStudentDestroyAPIView(DestroyAPIView):  # DELETE
    serializer_class = UserSerializer
    queryset = User.objects.filter(role=User.RoleType.STUDENT)
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        if not instance:
            raise NotFound('Student not found.')
        instance.delete()
