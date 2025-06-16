from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView

from apps.models import User
from apps.serializers import RegisterModelSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



@extend_schema(tags=['auth'], request=RegisterModelSerializer, responses=RegisterModelSerializer)
class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=['auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['auth'])
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['auth'])
class CustomTokenVerifyView(TokenVerifyView):
    pass