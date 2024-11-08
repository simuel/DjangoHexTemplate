from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

# Configuración del router para usar con DRF
router = DefaultRouter()
router.register(r'{{app_name}}', {{app_name.capitalize}}ViewSet, basename='{{app_name}}')

urlpatterns = [
    path('{{app_name}}/', include(router.urls)),
]
