from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework import permissions
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.views import Login, logout

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion publica de API de ecomerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dejonada12@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    #URL de la Documentacion de la API
    re_path(r'swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name = 'login'),
    path('logout/', logout.as_view(), name = 'logout'),
    path('usuario/', include('apps.users.api.urls')),
    path('product/', include('apps.Products.api.router')),
   
]
