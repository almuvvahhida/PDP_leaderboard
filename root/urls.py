from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('superuser.urls')),

    path('api/v1/', include('authentication.urls'))
]

urlpatterns+=[
    path("api/v1/",include("student.urls"))
]