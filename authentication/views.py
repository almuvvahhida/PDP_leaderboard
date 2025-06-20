from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.models import Session, User
from superuser.serializers import SessionSerializer


# Create your views here.

@extend_schema(tags=['auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        phone = request.data.get("phone")
        user = User.objects.filter(phone=phone).first()
        device_info = request.META.get('HTTP_USER_AGENT')
        device_ip = request.META.get('REMOTE_ADDR')
        session = Session.objects.filter(device_name=device_info)
        session_list = Session.objects.filter(user=user)
        if not session.exists():
            if len(session_list) >= 3:
                response = Response(SessionSerializer(instance=session_list, many=True).data)
            else:
                Session.objects.create(user=user, device_name=device_info, ip_address=device_ip)
        return response


@extend_schema(tags=['auth'])
class CustomTokenRefreshView(TokenRefreshView):
    pass

@extend_schema(tags=['auth'])
class SessionDestroyAPIView(DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'session_pk'


