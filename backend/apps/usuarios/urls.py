from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AuditLogViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')
router.register(r'audit-logs', AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]
